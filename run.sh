#!/bin/bash
if [ -d .env ]
then
        echo "virtual env exists"
else
	python3 -m venv .env
	source .env/bin/activate
fi

python3 script.py


