install:
	uv sync

start:
	uv run start

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check VD_games

lint-fix:
	uv run ruff check --fix VD_games




