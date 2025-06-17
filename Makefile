PYTHON = python3
PROJECT_DIR = app
SETTINGS_FILE = pyproject.toml

.PHONY: format lint secure type-check enable-pre-commit-hooks install build help

help:
	@echo "Available commands:"
	@echo "  make format  - Format the code with black and isort"
	@echo "  make lint    - Lint the code with flake8"
	@echo "  make secure    - Check security issues via bandit"
	@echo "  make type-check    - Check type issues via mypy"
	@echo "  make enable-pre-commit-hooks    - Enable pre commit hook"
	@echo "  make build  - Make build project"
	@echo "  make install  - Install development stage dependencies"
	@echo "  make help    - Show this help message"

format:
	$(PYTHON) -m isort $(PROJECT_DIR) --settings $(SETTINGS_FILE)
	$(PYTHON) -m autoflake $(PROJECT_DIR) --config $(SETTINGS_FILE)
	$(PYTHON) -m black $(PROJECT_DIR) --config $(SETTINGS_FILE)
	$(PYTHON) -m autopep8 $(PROJECT_DIR) --global-config $(SETTINGS_FILE)

lint:
	flake8 --config=.flake8.cfg
	$(PYTHON) -m black $(PROJECT_DIR) --check --diff --config $(SETTINGS_FILE)
	$(PYTHON) -m isort $(PROJECT_DIR) --check --diff --settings $(SETTINGS_FILE)

secure:
	$(PYTHON) -m bandit -r $(PROJECT_DIR) --config ${SETTINGS_FILE}

type-check:
	$(PYTHON) -m mypy $(PROJECT_DIR) --config ${SETTINGS_FILE}

enable-pre-commit-hooks:
	${PYTHON} -m pre_commit install

install:
	cd ${PROJECT_DIR} && pip install -r requirements.txt

build:
	cd ${PROJECT_DIR} && ${PYTHON} manage.py runserver

migrate-all:
	cd ${PROJECT_DIR} && python3 manage.py makemigrations spy && python3 manage.py migrate