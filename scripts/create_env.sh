#!/bin/bash

VENV_DIR="OzPr"
if [[ $# -eq 1 ]]; then
    VENV_DIR="$1"
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "Создание виртуального окружения: $VENV_DIR"
    python3 -m venv $VENV_DIR > /dev/null
    source $VENV_DIR/bin/activate
elif [[ "$VIRTUAL_ENV" != *"/$VENV_DIR"* && -f "$VENV_DIR/bin/activate" ]]; then
    echo "Активация виртуального окружения"
    source $VENV_DIR/bin/activate
fi
