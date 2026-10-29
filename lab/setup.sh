#!/usr/bin/env bash
# WiseQ test lab — one-command setup for a machine with Docker.
#
#   ./setup.sh          build the image and run the demo
#   ./setup.sh test     build the image and run the golden test suite
#   ./setup.sh shell    build the image and drop into a shell
#
# Requires: Docker with the Compose plugin. Nothing else.
set -euo pipefail

cd "$(dirname "$0")"

MODE="${1:-demo}"

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is not installed. Install Docker Desktop (Windows/Mac) or Docker Engine (Linux):" >&2
  echo "  https://docs.docker.com/get-docker/" >&2
  exit 1
fi

if ! docker compose version >/dev/null 2>&1; then
  echo "Docker Compose plugin not found. Install it: https://docs.docker.com/compose/install/" >&2
  exit 1
fi

echo "==> Building the lab image (first run takes a minute)"
docker compose build

case "$MODE" in
  demo)
    echo "==> Running the synthetic scenarios"
    docker compose run --rm demo
    ;;
  test)
    echo "==> Running the golden test suite"
    docker compose run --rm demo pytest -q -p no:cacheprovider
    ;;
  shell)
    echo "==> Opening a shell inside the lab (the repo is mounted read-only at /app)"
    docker compose run --rm --entrypoint bash demo
    ;;
  *)
    echo "Unknown mode '$MODE'. Use: demo | test | shell" >&2
    exit 2
    ;;
esac

echo
echo "==> Done. Nothing here touches a production system."
