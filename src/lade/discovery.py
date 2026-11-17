"""Process discovery and the quality measures used to compare models (milestone M2)."""
import pandas as pd
import pm4py

ALGORITHMS = {
    "Inductive Miner": lambda log: pm4py.discover_petri_net_inductive(log, noise_threshold=0.0),
    "Inductive Miner, 20% noise filter": lambda log: pm4py.discover_petri_net_inductive(log, noise_threshold=0.2),
    "Heuristics Miner": lambda log: pm4py.discover_petri_net_heuristics(log),
}


def quality(log, net, im, fm):
    """Token-based fitness and precision in %, their harmonic mean (F1), model size and soundness."""
    fit = pm4py.fitness_token_based_replay(log, net, im, fm)
    f, p = fit["log_fitness"], pm4py.precision_token_based_replay(log, net, im, fm)
    return {"fitness %": 100 * f, "fitting traces %": fit["percentage_of_fitting_traces"], "precision %": 100 * p,
            "F1 %": 100 * 2 * f * p / (f + p) if f + p else 0.0,
            "transitions": len(net.transitions), "places": len(net.places), "arcs": len(net.arcs),
            "sound": bool(pm4py.check_soundness(net, im, fm)[0])}


def compare(logs, eval_logs=None):
    """Discover one model per (log, algorithm) and measure it on the same log, or on eval_logs[name] if given
    (a case sample, for logs where replay is slow). Returns the comparison table and the models."""
    rows, models, eval_logs = [], {}, eval_logs or {}
    for log_name, log in logs.items():
        for algo, discover in ALGORITHMS.items():
            models[log_name, algo] = discover(log)
            measured = eval_logs.get(log_name, log)
            rows.append({"log": log_name, "algorithm": algo, **quality(measured, *models[log_name, algo])})
    return pd.DataFrame(rows), models
