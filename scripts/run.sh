#!/bin/bash

cd "$(dirname "$0")/.."

. scripts/create_env.sh
pip3 install .
