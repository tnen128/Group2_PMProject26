"""Process maps labelled with percentages instead of counts, with a legend on the right."""
import graphviz
import pandas as pd


def _pct(p):
    return "<0.1%" if p < 0.1 else f"{p:.1f}%" if p < 10 else f"{p:.0f}%"


def _fill(p):
    """Light to dark blue with the share of cases."""
    lo, hi = (232, 240, 250), (60, 110, 175)
    return "#" + "".join(f"{round(a + (b - a) * p / 100):02x}" for a, b in zip(lo, hi))


def save_dfg_percent(log, path, title="", unit="cases"):
    """Directly-follows graph of a PM4Py-formatted log (sorted by case and time).

    Box: share of cases that contain the activity. Arrow: share of cases in which the
    first activity is directly followed by the second (at least once)."""
    case, act = log["case:concept:name"], log["concept:name"]
    n = case.nunique()
    pairs = pd.DataFrame({"case": case, "a": act, "b": act.groupby(case).shift(-1)}).dropna()
    edges = pairs.drop_duplicates().groupby(["a", "b"]).size() / n * 100
    nodes = pd.DataFrame({"case": case, "a": act}).drop_duplicates().groupby("a").size() / n * 100
    starts = act[~case.duplicated()].value_counts() / n * 100
    ends = act[~case.duplicated(keep="last")].value_counts() / n * 100

    g = graphviz.Digraph(graph_attr={"rankdir": "LR", "label": title, "labelloc": "t", "fontname": "Helvetica",
                                     "fontsize": "16", "nodesep": "0.4", "ranksep": "0.9"},
                         node_attr={"shape": "box", "style": "rounded,filled", "fontname": "Helvetica"},
                         edge_attr={"fontname": "Helvetica", "fontsize": "10", "color": "#555555"})
    g.node("start", "", shape="circle", width="0.3", style="filled", fillcolor="#2e7d32")
    g.node("end", "", shape="doublecircle", width="0.25", style="filled", fillcolor="#c62828")
    for a, p in nodes.items():
        g.node(a, f"{a}\n{_pct(p)}", fillcolor=_fill(p), fontcolor="white" if p > 60 else "black")
    for src, dst, share in ([("start", a, p) for a, p in starts.items()] + [(a, b, p) for (a, b), p in edges.items()]
                            + [(a, "end", p) for a, p in ends.items()]):
        g.edge(src, dst, label=_pct(share), penwidth=f"{0.6 + 4 * share / 100:.2f}")
    legend = (f"<<table border='1' cellborder='0' cellpadding='4' bgcolor='#fafafa'>"
              f"<tr><td align='left'><b>How to read</b></td></tr>"
              f"<tr><td align='left'>Box: activity, % of {unit} in which it occurs</td></tr>"
              f"<tr><td align='left'>Arrow: directly followed by,<br align='left'/>% of {unit} in which this happens</td></tr>"
              f"<tr><td align='left'>Darker box, thicker arrow: more {unit}</td></tr>"
              "<tr><td align='left'><font color='#2e7d32'>●</font> start   <font color='#c62828'>◉</font> end</td></tr>"
              "</table>>")
    g.node("legend", legend, shape="plaintext", style="")
    g.edge("end", "legend", style="invis")  # keeps the legend on the right
    g.render(outfile=str(path), format="png", cleanup=True)
