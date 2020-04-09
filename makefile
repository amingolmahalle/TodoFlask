#!/bin/sh
dev:
	python src/main.py --log=INFO
run:
	cd src && ../.venv/bin/gunicorn -w 4 -b 127.0.0.1:5050 main
test:
	python -m unittest discover -s src -p '*test.py'