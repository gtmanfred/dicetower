test:
	poetry run coverage run -m pytest -v

syntax:
	poetry run black --check .

coverage:
	poetry run coverage report
	poetry run coverage xml
