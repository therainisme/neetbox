#!/bin/sh

# project root
cd $(dirname $0)/..

tmux new-session -d -s neetbox
tmux send 'cd tests/client' ENTER
tmux send 'neet serve' ENTER
tmux split-window -h
tmux send 'cd tests/client' ENTER
tmux send 'python test.py' ENTER
tmux split-window -f
tmux send 'cd frontend' ENTER
tmux send 'yarn dev' ENTER
tmux set mouse on
tmux a -t neetbox
