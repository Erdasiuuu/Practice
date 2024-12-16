#!/bin/bash

ENV_NAME="env_practice"
if [[ $# -eq 1 ]]; then
    ENV_NAME="$1"
fi

if [ -z "$(conda env list | grep -w "$ENV_NAME")" ]; then
    echo "Создание виртуального окружения: $VENV_DIR"
    conda create -n $ENV_NAME python=3.10 anaconda
    conda activate $ENV_NAME
    pip install -r requirements.txt
elif [[ "$CONDA_DEFAULT_ENV" != "$ENV_NAME" ]]; then
    echo "Активация виртуального окружения"
    conda activate $ENV_NAME
fi
