#!/usr/bin/env bash

# Don't let CDPATH interfere with the cd command
unset CDPATH
cd "$(dirname "$0")"

# activate the python virtualenv
#source ".venv/bin/activate"

# activate local python version
pyenv local 3.8.2

# Execute the bot
exec python ./run.py
