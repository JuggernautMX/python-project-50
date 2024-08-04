install:
	poetry install

gendiff:
	poetry run gendiff

build:
	rm -f ./dist/*
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 gendiff
