#!/bin/bash
# entrypoint.sh

set -eu
tmux attach

exec "$@"
