#!/bin/bash
# entrypoint.sh

node /home/ctf/app/web-terminal-server.js

set -eu
tmux attach

exec "$@"
