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
| `adapters/vendor/` | Read stubs (fail-closed until Wave 1 keys) |
| `fixtures/` | Synthetic catalog, **32** school mails, tariffs, accounts |
| `scenarios/` | Experiment A/B/C runners |
| `tests/` | Golden pytest suite (incl. eval + vendor stubs) |
| `hermes/` | Desktop skills + [DEMO-SCRIPT](hermes/DEMO-SCRIPT.md) |
| `scripts/gen_school_goldens.py` | Regenerate mailbox goldens |

## Hermes Desktop

```text
hermes --profile wiseq-lab doctor
hermes desktop --cwd <absolute-path-to>/lab
```

YOLO **off**. Demo: [`hermes/DEMO-SCRIPT.md`](hermes/DEMO-SCRIPT.md) · Notes: [`docs/50-evidence/06-hermes-desktop.md`](../docs/50-evidence/06-hermes-desktop.md).

## Experiments

| ID | Command |
| :--- | :--- |
| A School | `pytest tests/test_scenario_a_school.py -q` |
| B Spine | `pytest tests/test_scenario_b_catalog.py -q` |
| C Shipping | `pytest tests/test_scenario_c_shipping.py -q` |
