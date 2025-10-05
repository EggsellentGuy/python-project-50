install:
	uv sync --dev

lint:
	uv run ruff check .

check:
	make lint
	uv run pytest -q

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

