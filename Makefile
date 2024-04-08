format_code:
	poetry run isort .
	poetry run black .

quality:
	poetry run black --check .
	poetry run flake8 --max-line-length=99 --exclude .git,__pycache__,.venv
	poetry run mypy assessment --allow-untyped-decorators

task1:
	poetry run python main.py --input=input  --output=output/recipes --task=task1

task2:
	 poetry run python main.py --input=output/recipes --output=output/cook_time_difficulty --task=task2
