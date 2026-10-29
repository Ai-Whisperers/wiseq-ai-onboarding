# WiseQ test lab — self-contained demo image.
#
# Zero-install: one command and Rob can run the whole lab on his own machine.
# NO production credentials, NO live vendor calls. Everything is synthetic.
#
#   docker compose run --rm demo
#
FROM python:3.12-slim

LABEL org.opencontainers.image.title="WiseQ test lab" \
      org.opencontainers.image.description="Synthetic WiseQ workflow lab — no production credentials" \
      org.opencontainers.image.licenses="UNLICENSED"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

WORKDIR /app

# Dependencies first so the layer caches across code edits.
COPY pyproject.toml ./
RUN pip install --no-cache-dir "pytest>=8.0"

# The lab itself.
COPY . .

# Sanity check at build time: the suite must pass before the image is shipped.
# -p no:cacheprovider: the image runs with a read-only filesystem, so pytest
# must not try to write its cache. The audit log is redirected via
# WISEQ_EVAL_OUT in docker-compose.yml.
RUN PYTHONPATH=/app python -m pytest -q -p no:cacheprovider

# Default: run the demo. Override with:
#   docker compose run --rm demo pytest -q
#   docker compose run --rm demo python -m wiseq_demo --json
CMD ["python", "wiseq_demo.py"]
