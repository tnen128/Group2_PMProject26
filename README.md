# Group B – Process Mining Project WS26/27 (TUM)

Mohamed Badawy (`tnen128`) · Abdelrahman ElKoussy (`akoussy`)

Dataset: **LaDe** – last-mile parcel pickups from Cainiao (Alibaba), May–Oct 2022.
We build an event log from the raw data, discover the process (BPMN) and do process enhancement (Option 2): bottlenecks and which attributes (courier, region, AOI) relate to late pickups.

## Layout

| Path | What |
|---|---|
| `docs/roadmap/` | Roadmap submitted on Moodle |
| `notebooks/01_explore_jilin_pickup.ipynb` | Data quality, plan vs reality, two candidate event logs, first discovery |
| `notebooks/02_event_log.ipynb` | Event log v1: building decisions, case notion (convergence/divergence), six activities, preprocessing pipeline with the effect of each step |
| `docs/milestones.md`, `docs/consultations.md` | Project plan and consultation log |
| `outputs/figures/`, `outputs/tables/` | Figures and tables used in the slides and the report |
| `outputs/metadata_basics.csv` | First numbers for the 37-attribute metadata table |
| `data/` | Raw CSVs and XES exports (not committed, created by the notebook) |

## Run

```bash
uv venv -p 3.11 .venv && uv pip install -p .venv/bin/python -r requirements.txt
brew install graphviz   # needed for PM4Py process map images
.venv/bin/jupyter nbconvert --to notebook --execute --inplace notebooks/01_explore_jilin_pickup.ipynb
.venv/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=1800 notebooks/02_event_log.ipynb
```

The notebook downloads `pickup_jl.csv` and `delivery_jl.csv` from [Cainiao-AI/LaDe on Hugging Face](https://huggingface.co/datasets/Cainiao-AI/LaDe) on first run. Notebook 02 takes about 3 minutes and writes event log v1 to `data/processed/lade_jl_pickup_parcel_v1.xes.gz`.

## Commits

Push meaningful progress at least weekly. For pair work, end the commit message with
`Co-authored-by: Name <email>` for everyone who took part.
