# WiseQ test lab

Isolated synthetic environment for WiseQ workflows. **No production credentials or MCP connections.**

## Setup

```bash
cd lab
python -m pip install -e ".[dev]"
pytest -q
```

Reset fixtures (deterministic): delete `eval/out/` if present; fixtures under `fixtures/` are versioned.

## Layout

| Path | Role |
| :--- | :--- |
| `contracts/` | Provider Protocols |
| `adapters/fixture/` | Deterministic mocks (`simulated=true`) |
| `adapters/oss/` | Placeholders for local OSS apps |
| `adapters/vendor/` | Placeholders for approved vendor sandboxes |
| `fixtures/` | Synthetic catalog, mailbox, tariffs, accounts |
| `scenarios/` | Experiment A/B/C runners |
| `tests/` | Golden pytest suite |
| `hermes/` | Desktop skills + memory seed |

## Hermes Desktop

```text
hermes --profile wiseq-lab doctor
hermes desktop --cwd <absolute-path-to>/lab
```

YOLO **off**. See [`docs/50-evidence/06-hermes-desktop.md`](../docs/50-evidence/06-hermes-desktop.md).

## Experiments

| ID | Command |
| :--- | :--- |
| A School | `pytest tests/test_scenario_a_school.py -q` |
| B Spine | `pytest tests/test_scenario_b_catalog.py -q` |
| C Shipping | `pytest tests/test_scenario_c_shipping.py -q` |
