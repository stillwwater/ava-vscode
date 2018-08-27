#!/bin/bash

set -e

cd build
python3 ava.py blue.var ../themes/ava-blue.json
python3 ava.py midnight.var ../themes/ava-midnight.json
