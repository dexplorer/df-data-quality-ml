install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py &&\
	pylint --disable=R,C dqml_app/*.py &&\
	pylint --disable=R,C dqml_app/*/*.py &&\
	pylint --disable=R,C dqml_app/tests/*.py
	# pylint --disable=R,C dqml_app.py

test:
	python -m pytest -vv --cov=dqml_app/utils dqml_app/tests/test_misc.py
	# python -m pytest -vv --cov=dqml_app_core dqml_app/tests/test_dqml_app_core.py

format:
	black *.py &&\
	black dqml_app/*.py &&\
	black dqml_app/*/*.py &&\
	black dqml_app/tests/*.py

all:
	install lint format test
	