#!/usr/bin/env bash
# WiseQ test lab — health check. Verifies the image exists and the suite passes.
#
#   ./status.sh
set -euo pipefail

cd "$(dirname "$0")"

if ! command -v docker >/dev/null 2>&1; then
  echo "FAIL  docker not installed"
  exit 1
fi

if ! docker image inspect wiseq-lab:latest >/dev/null 2>&1; then
  echo "FAIL  image wiseq-lab:latest not built yet — run ./setup.sh"
  exit 1
fi

echo "OK    image wiseq-lab:latest present"

if docker compose run --rm demo pytest -q -p no:cacheprovider >/dev/null 2>&1; then
  echo "OK    golden test suite passes inside the container"
else
  echo "FAIL  golden test suite fails inside the container"
  exit 1
fi

echo "OK    lab is healthy"
