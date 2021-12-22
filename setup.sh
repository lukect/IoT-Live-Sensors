#!/bin/bash

rm -rf venv
rm -rf __pycache__
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt