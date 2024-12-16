#!/bin/bash

VENV_DIR="OzPr"
if [[ $# -eq 1 ]]; then
    VENV_DIR="$1"
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "Создание виртуального окружения: $VENV_DIR"
    virtualenv $VENV_DIR > /dev/null
    source $VENV_DIR/bin/activate
    pip install -r requirements.txt > /dev/null
elif [[ "$VIRTUAL_ENV" != *"/$VENV_DIR"* && -f "$VENV_DIR/bin/activate" ]]; then
    echo "Активация виртуального окружения"
    source $VENV_DIR/bin/activate
fi
