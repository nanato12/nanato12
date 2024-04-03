.PHONY: init
init:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

.PHONY: lint
lint:
	rm -rf .mypy_cache
	black .
	flake8 .
	isort .
	mypy .
	npm run lint

.PHONY: generate
generate:
	python generate.py
