#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_timer/ tests/

black democritus_timer/ tests/

mypy democritus_timer/ tests/

pylint --fail-under 9 democritus_timer/*.py

flake8 democritus_timer/ tests/

bandit -r democritus_timer/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_timer/ tests/
