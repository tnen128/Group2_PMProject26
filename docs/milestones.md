# Project plan and milestones

**Group B · Process Mining Project WS 2026/27 · TUM**
Mohamed Badawy (`tnen128`) · Abdelrahman ElKoussy (`akoussy`)

Dataset: **LaDe** (Cainiao last-mile parcels, May–Oct 2022). Focus: courier routing, batching and late pickups.
Tasks: 1 Preprocessing (XES event log + metadata table), 2 Process discovery (BPMN), 3.2 Process enhancement (Option 2).

Status: 12 Nov 2026, after the first consultation (see `docs/consultations.md`). This plan refines the roadmap submitted on Moodle (`docs/roadmap/`) and keeps its phases and owners. We update it after every consultation.

## 1. Fixed dates

| Date | Event | Project week |
|---|---|---|
| Thu 12 Nov | Consultation | W2 |
| Wed 18 Nov | Consultation | W3 |
| Tue 24 Nov | Consultation | W4 |
| **Wed 2 Dec** | **Mid-term presentation (7 min)** | W5 |
| Wed 9 Dec | Consultation | W6 |
| 21 Dec – 3 Jan | Christmas break, no milestones planned | W8–W9 |
| Wed 13 Jan | Consultation | W11 |
| Wed 20 Jan | Consultation | W12 |
| **Thu 28 Jan** | **Final presentation (15 min)** | W13 |
| Wed 3 Feb | Consultation | W14 |
| **Thu 11 Feb** | **Submission of the report (LNCS, max. 15 pages)** | W15 |

Project weeks follow the roadmap: W1 = 2–8 Nov, W2 = 9–15 Nov, …, W7 = 14–20 Dec, W10 = 4–10 Jan, W15 = 8–14 Feb.
We attend the consultations as a group and in person, with a few slides and current outputs (section 4).

## 2. Milestones

| # | Milestone | Weeks | Shown at | Owner |
|---|---|---|---|---|
| M0 | Setup and first exploration | W1–W2 | 12 Nov | both |
| M1 | Preprocessing pipeline and event log v1 | W3–W4 | 18 Nov, 24 Nov | Mohamed |
| M2 | First process discovery | W3–W5 | 24 Nov, 2 Dec | Abdelrahman |
| M3 | Mid-term presentation | W5 | 2 Dec | both |
| M4 | Final event log, metadata table, final BPMN | W6–W7 | 9 Dec | Mohamed (log, metadata), Abdelrahman (BPMN) |
| M5 | Process enhancement (Option 2) | W6–W11 | 9 Dec, 13 Jan | both, split in two parts |
| M6 | Final presentation | W12–W13 | 20 Jan, 28 Jan | both |
| M7 | Report and submission | W7–W15 | 13 Jan, 3 Feb, 11 Feb | both |

### M0 · Setup and first exploration (W1–W2, shown 12 Nov)

- Deliverables: repository and roadmap; exploration notebook for the Jilin pickups with data quality checks, plan vs. reality, two candidate event logs (case = parcel, case = courier-day) exported as XES, and a first DFG and BPMN (Abdelrahman). Review of the notebook and this milestone plan (Mohamed).
- Done when: the notebook runs end to end from the raw data; the open questions in section 5 are answered in the consultation and recorded in `docs/consultations.md`.

### M1 · Preprocessing pipeline and event log v1 (W3–W4, shown 18 and 24 Nov) — Mohamed

- Deliverables:
  - Preprocessing as code in `src/lade/` (one function per step) that rebuilds the event log from the raw CSV with one command.
  - `docs/preprocessing_decisions.md`: one entry per decision (case notion, case day, timestamp source, missing year, event order for equal timestamps, implausible durations, definition of late), each with alternatives, reason and effect.
  - Step table with parcels, cases, events and variants before and after each step.
  - Event log v1 as XES for Jilin; notebook `02_event_log.ipynb`.
  - Progress 12 Nov: `02_event_log.ipynb` follows the course preprocessing tutorial: building decisions (Jans, Soffer & Jouck), case notion with convergence and divergence, a parcel log with six activities, a pipeline of filtering, transformation, abstraction and enrichment steps with the effect of each step, FEEED features, and XES v1 (`lade_jl_pickup_parcel_v1.xes.gz`). Still open: moving the pipeline to `src/lade/`, the decisions document, and the Disco check.
- Done when: one command reproduces the log from raw data; every decision has a documented effect in numbers; the XES file loads in PM4Py and Disco with the same case and event counts.

### M2 · First process discovery (W3–W5, shown 24 Nov and 2 Dec) — Abdelrahman

- Deliverables:
  - Discovery functions in `src/lade/discovery.py` and notebook `03_discovery.ipynb`.
  - Comparison of at least two discovery algorithms (Inductive Miner, Heuristics Miner, plus the DFG) on the parcel log with six activities and on the courier-day view, at least two abstraction levels (single events, batches of consecutive accepts and pickups, refined activity labels), with fitness, precision and model size.
  - One candidate BPMN model (`.bpmn` and image) and a short analysis of how preprocessing decisions change the model.
  - LNCS report skeleton in `report/`.
- Done when: the comparison table exists; the candidate BPMN opens in a BPMN editor; the notebook runs on event log v1.

### M3 · Mid-term presentation (2 Dec) — both

- Deliverables: a 7-minute presentation with results so far, tools used, who did what and who does what next. Mohamed presents data, event log design and preprocessing; Abdelrahman presents discovery and tools.
- Done when: one timed rehearsal stays within 7 minutes; every number on the slides comes from a file in `outputs/`; the repository is up to date and tagged `midterm`.

### M4 · Final event log, metadata table and final BPMN (W6–W7, shown 9 Dec)

- Deliverables (Mohamed): final event log, frozen on 18 Dec and exported as compressed XES; pipeline run for further cities for comparison; event log metadata table with all 37 attributes in the format of the Zenodo collection (Costa et al., 2025); first draft of report section 2.
- Deliverables (Abdelrahman): final BPMN model(s) with every manual change listed in `docs/bpmn_manual_changes.md`; first draft of report section 3.
- Done when: the log is tagged `log-final` and later analyses use only this version; all 37 metadata attributes are filled or marked N/A with a reason; the edited BPMN is replayed on the log and its fitness is reported.

### M5 · Process enhancement, Option 2 (W6–W11, shown 9 Dec and 13 Jan)

- Part A, bottlenecks, batching and routing (Abdelrahman): where time is lost between accepting and picking up an order; performance view of the process; effect of batch size, daily workload and time of day; route features per courier-day (stops, revisited areas, distance between consecutive pickups). Notebook `05_bottlenecks.ipynb`.
- Part B, attributes related to delays (Mohamed): relation of courier, region, AOI, AOI type, time window, time of day and city to delays, with group sizes and effect sizes; ranking of the attributes; comparison across cities. Notebook `06_delay_attributes.ipynb`.
- Done when: each part has at least three quantified findings with a figure, computed on the frozen log; drafts of report sections 4.1 and 4.2 exist.

### M6 · Final presentation (dry run 20 Jan, presentation 28 Jan) — both

- Deliverables: 15-minute presentation; each member presents about half. Mohamed: event log and attributes related to delays. Abdelrahman: discovery, BPMN and bottlenecks. Joint conclusion.
- Done when: a timed rehearsal stays within 15 minutes; the deck is in the repository the day before.

### M7 · Report and submission (drafts 13 Jan and 3 Feb, submission 11 Feb) — both

- Deliverables: report in LNCS format with at most 15 pages; XES event log; BPMN model(s); metadata table in the appendix; documentation of each member's role and activities.
- Plan: sections 2 and 3 drafted by 20 Dec, section 4 by 17 Jan, complete draft by 31 Jan, feedback on 3 Feb, final version on 9 Feb (two days of buffer).
- Done when: the PDF builds from `report/`, respects the page limit, and every number can be traced to a notebook; the repository is tagged `submission`.

## 3. Who owns what

Each member owns code, report sections and presentation parts. The owner writes and commits the work; the other member reviews the pull request.

| | Mohamed Badawy | Abdelrahman ElKoussy |
|---|---|---|
| Project task | 1 Preprocessing: event log, XES, metadata table | 2 Process discovery: BPMN |
| Enhancement (3.2) | Attributes related to delays | Bottlenecks, batching and routing |
| Code (`src/lade/`) | `schema.py`, `preprocess.py`, `metadata.py`, `delays.py` | `discovery.py`, `performance.py` |
| Notebooks | `02_event_log`, `04_final_log_metadata`, `06_delay_attributes` | `01_explore_jilin_pickup`, `03_discovery`, `05_bottlenecks` |
| Documents | `milestones.md`, `preprocessing_decisions.md` | `consultations.md`, `bpmn_manual_changes.md`, `README.md` |
| Report sections | 2 Data and event log · 4.2 Attributes related to delays · Appendix: metadata table | 1 Introduction · 3 Process discovery · 4.1 Bottlenecks, batching and routing · 5 Discussion and conclusion |
| Mid-term (7 min) | Data, event log design, preprocessing decisions | Discovery, BPMN, tools; assembles the slides |
| Final (15 min) | Event log; attributes related to delays; assembles the slides | Discovery and BPMN; bottlenecks, batching and routing |
| Review | Abdelrahman's pull requests | Mohamed's pull requests |
| Role documentation | `docs/activity_log_mohamed.md` | `docs/activity_log_abdelrahman.md` |

The two parts meet at one interface: `src/lade/schema.py` fixes the column names, file paths and loading functions of the event log, so discovery and enhancement do not depend on the internals of the preprocessing.

## 4. What we bring to each consultation

| Date | Mohamed | Abdelrahman |
|---|---|---|
| 12 Nov | Data and quality, event log design | Plan vs. reality, first DFG and BPMN, questions |
| 18 Nov | Pipeline as code, first step table, case-day analysis | First algorithm comparison, report skeleton |
| 24 Nov | Event log v1 (XES), preprocessing decisions | Candidate BPMN with quality measures, mid-term outline |
| 2 Dec | Mid-term presentation | Mid-term presentation |
| 9 Dec | Final log proposal, metadata table draft, city overview | Final BPMN and manual changes, first bottleneck results |
| 13 Jan | Attributes related to delays, draft of section 2 | Bottlenecks, batching and routing, draft of section 3 |
| 20 Jan | Dry run of the final presentation | Dry run of the final presentation |
| 3 Feb | Complete report draft, questions on submission | Complete report draft, questions on submission |

## 5. Open decisions and our defaults

The plan works for either answer. We follow the default unless advised otherwise, and record the outcome in `docs/consultations.md`.

| # | Question | Default | If decided differently |
|---|---|---|---|
| D1 | Case notion | Updated after 12 Nov: **parcel** as the main log, with six activities from the six timestamp columns (accept, accept GPS fix, window opens, pick up, pickup GPS fix, window closes): no convergence, no divergence, 27 variants after preprocessing. The courier-day is kept as a second view for batching and is labelled as divergent (a median of 8 parcels per case causes false loops). | The event table is independent of the case notion, so another case (courier, pickup round, object-centric) is a change in the last pipeline step. |
| D2 | Definition of "late" | Report both: pickup after the promised window (0.2%) and a long wait from accept to pickup (above the 90th percentile, about 6 h in Jilin). The long wait is the main delay measure because it has enough cases. Early pickups (29%) are reported as deviation from the plan. | The delay measure is one setting. If only "after the window" counts, Jilin has about 500 late parcels, so Part B of M5 needs further cities (see D4). |
| D3 | Combine pickup and delivery | Pickup only. The delivery data has no promised window, parcels are not linked between the two files, and in a first check only 4 of 665 Jilin pickup couriers also appear in the delivery data. | A separate delivery log built with the same pipeline, used for comparison. |
| D4 | Jilin or more cities | Jilin as the main log and the submitted XES. Other cities run through the same pipeline after the mid-term and are used for comparison in M5. | A larger city as the main log: same pipeline, larger XES file. |
| D5 | GPS events | No trajectory events. The GPS fields of each parcel are used for validation and for distances. | A time-boxed test of events from the courier trajectories in M4, added as a new activity. |

Further points to clarify: how the XES file should be handed in (compressed, about 15 MB for Jilin), whether the appendix counts towards the 15 pages, and the format of the role and activity documentation.

## 6. Working agreements

- Each member pushes meaningful commits at least weekly. Pair work carries a `Co-authored-by:` line.
- All work goes through pull requests; the other member reviews, runs the checks and merges.
- The repository is up to date the day before each consultation and presentation.
- The event log is reproducible from the raw data with one command; raw data and large intermediate files are not committed.
- Numbers on slides and in the report come from files in `outputs/`, produced by a notebook that runs end to end.
- Requests to change the event log go through GitHub issues until the freeze on 18 Dec.

## 7. Risks

| Risk | Mitigation |
|---|---|
| The process has only two recorded activities, so the model can become trivial. | Addressed on 12 Nov: all six timestamp columns become activities (window and GPS fix events), giving 27 parcel variants; refined activity labels and courier-level rounds as further options (M2). |
| Very few pickups are late with respect to the window. | Two delay measures (D2); further cities for more cases (D4). |
| Timestamps have minute resolution; 11% of events share a minute with another event of the same courier-day. | Fixed and documented ordering rule; its effect on variants is measured in M1. |
| Event log changes late and results become inconsistent. | Freeze on 18 Dec (`log-final`); all enhancement results are recomputed on the frozen log. |
| Christmas break and exam period shorten January. | Sections 2 and 3 drafted before the break; complete draft on 31 Jan; final version two days before the deadline. |
