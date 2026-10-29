from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = LAB_ROOT / "fixtures"

# The bundle spine + component registry are vendored into lab/fixtures/ so the
# lab is self-contained and runs identically inside the Docker image (which
# contains only lab/). The repo-root copies remain the source of truth; the
# vendored pair is refreshed by scripts/sync_spine_fixtures.py.
SPINE_CSV = FIXTURES / "wiseq-bundle-spine.csv"
REGISTRY_CSV = FIXTURES / "wiseq-component-registry.csv"
