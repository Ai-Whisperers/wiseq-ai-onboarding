# Milestone 1 acceptance checklist

| # | Criterion | How to verify |
| ---: | :--- | :--- |
| 1 | Synthetic knowledge base accessible | `lab/fixtures/` + `lab/hermes/memory/SEED.md` |
| 2 | Operational Q&A with evidence | Hermes Desktop + `wiseq-operations` skill |
| 3 | Three E2E scenarios | `pytest tests/test_scenario_a_school.py tests/test_scenario_b_catalog.py tests/test_scenario_c_shipping.py -q` |
| 4 | Delegation to specialized skill | Coordinator → `school-pipeline` / `shipping-econ` / `catalog-integrity` |
| 5 | Recurring-style report | `ops-briefing` skill on fixtures |
| 6 | Validation + approval gates | Reject without APPROVE; YOLO off |
| 7 | Rerunnable results | pytest green twice; idempotent invoice test |

Profile: `wiseq-lab` · YOLO off · `hermes desktop --cwd <repo>/lab`
