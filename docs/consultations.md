# Consultation log

One entry per consultation: what we showed, the feedback, and what we changed.

## Thu 12 Nov 2026 · first consultation

**Shown:** notebook `01_explore_jilin_pickup.ipynb`: data quality of the Jilin pickups, plan vs. reality, two candidate event logs (case = parcel, case = courier-day), first DFG and BPMN, milestone plan.

**Feedback**

| # | Feedback | What we changed | Where |
|---|---|---|---|
| 1 | Follow the course notebooks when building and preprocessing the log. | Notebook 02 follows the structure of the preprocessing tutorial: building decisions, case notion, columns as events, then a pipeline of filtering, transformation, abstraction and enrichment, with the effect of each step and FEEED features. | `notebooks/02_event_log.ipynb` |
| 2 | Discuss case convergence and divergence for our log. | Parcel case: neither. Courier-day: no convergence, but strong divergence (median 8 parcels per case), so its loops are partly false. Courier-level events such as pickup rounds would converge in the parcel log (108,821 rounds copied into 261,801 parcels). | Notebook 02, section 3 |
| 3 | Two activities are too simple; the log should show the real, messy process and we should explain it. | All six timestamp columns become activities: accept, accept GPS fix, window opens, pick up, pickup GPS fix, window closes. The parcel log goes from 1 to 27 variants after preprocessing; the variants show early, on-time and late pickups and recording lags between GPS fix and app record. | Notebook 02, sections 4–8 |

**Decisions:** parcel is the main case notion; the courier-day stays as a second view for batching (D1 in `docs/milestones.md`).

**Also fixed:** in notebook 01, the step that merges repeated activities before the Inductive Miner dropped the first event of every courier-day. The corrected BPMN starts with *Accept order* (loop of accept and pick up), consistent with the DFG.

**Answers to our other questions** (delay definition, pickup and delivery, cities, GPS trajectories, XES hand-in, page limit): to be added.
