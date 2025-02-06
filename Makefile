install: requirements.txt
	pip install --upgrade pip &&\
	pip install -r requirements.txt

setup: 
	# python setup.py install
	pip install .

lint:
	pylint --disable=R,C *.py &&\
	pylint --disable=R,C dqml_app/*.py &&\
	pylint --disable=R,C dqml_app/*/*.py &&\
	pylint --disable=R,C dqml_app/tests/*.py

test:
	python -m pytest -vv --cov=dqml_app dqml_app/tests

format:
	black *.py &&\
	black dqml_app/*.py &&\
	black dqml_app/*/*.py &&\
	black dqml_app/tests/*.py

all: install setup lint format test
