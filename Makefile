install: pyproject.toml
	pip install --upgrade pip &&\
	pip install --editable . &&\
	pip install .[cli] &&\
	pip install .[api] &&\
	pip install .[test]
	
lint:
	pylint --disable=R,C src/dqml_app/*.py &&\
	pylint --disable=R,C src/dqml_app/*/*.py &&\
	pylint --disable=R,C tests/*.py

test:
	python -m pytest -vv --cov=dqml_app dqml_app/tests

format:
	black src/dqml_app/*.py &&\
	black src/dqml_app/*/*.py &&\
	black tests/*.py

all: install lint format test
