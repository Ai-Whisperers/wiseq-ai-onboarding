# WiseQ test lab

Isolated synthetic environment for WiseQ workflows. **No production credentials or MCP connections.**

## Run it with Docker (zero install)

The only prerequisite is Docker with the Compose plugin. Nothing else.

```bash
cd lab
./setup.sh          # build the image and run the three synthetic scenarios
./setup.sh test     # run the golden test suite inside the container
./status.sh         # verify the image exists and the suite passes
```

Or directly:

```bash
docker compose run --rm demo            # the scenarios
docker compose run --rm demo pytest -q  # the test suite
docker compose run --rm demo --json     # machine-readable output
```

The container runs with `network_mode: none` and `read_only: true`, and no
credentials are ever mounted into it. Live read-only keys arrive later into a
separate profile — never into this image.

## Run it with Python (no Docker)

```bash
cd lab
python -m pip install -e ".[dev]"
pytest -q
python wiseq_demo.py          # the same three scenarios
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
| `scripts/sync_spine_fixtures.py` | Refresh the vendored spine CSVs from `data/` (CI fails on drift) |
| `fixtures/wiseq-*.csv` | Vendored bundle spine + component registry (self-contained lab) |
| `wiseq_demo.py` | Demo CLI — runs the scenarios, prints them as text or JSON |
| `Dockerfile` · `docker-compose.yml` | Zero-install demo image |
| `setup.sh` · `status.sh` | One-command build/run and health check |

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
