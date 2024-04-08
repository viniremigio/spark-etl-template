IMAGE_NAME=spark_etl_template

.PHONY: format_code

format_code:
	docker-compose exec $(IMAGE_NAME) poetry run isort . && \
	docker-compose exec $(IMAGE_NAME) poetry run black .

quality:
	poetry run black --check .
	poetry run flake8 --max-line-length=99 --exclude .git,__pycache__,.venv
	poetry run mypy src --allow-untyped-decorators

task1:
	poetry run python main.py --input=input  --output=output/recipes --task=task1



