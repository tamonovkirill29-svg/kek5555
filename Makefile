install:
	uv sync

start:
	uv run start

build:
	uv build

package-install:
	uv tool install dist/*.whl





