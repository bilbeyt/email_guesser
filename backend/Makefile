.PHONY: lint test


CODE_DIRS = app/ scripts/

all: lint

lint:
	mypy $(CODE_DIRS)
	black --check --diff $(CODE_DIRS)
	flake8 $(CODE_DIRS)
	isort $(CODE_DIRS) --diff --check-only
	pylint $(CODE_DIRS)

test:
	pytest tests --cov app --cov scripts --cov-report term

