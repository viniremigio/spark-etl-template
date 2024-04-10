IMAGE_NAME=spark_etl_template

.PHONY: format_code lint run_etl start shell

shell:
	docker-compose exec -ti $(IMAGE_NAME) bash

start:
	docker-compose up -d

format_code:
	make start
	docker-compose exec $(IMAGE_NAME) poetry run isort . && \
	docker-compose exec $(IMAGE_NAME) poetry run black .

lint:
	make start
	docker-compose exec $(IMAGE_NAME) poetry run black --check . && \
	docker-compose exec $(IMAGE_NAME) poetry run flake8 --max-line-length=99 --exclude .git,__pycache__,.venv
	docker-compose exec $(IMAGE_NAME) poetry run mypy src --allow-untyped-decorators

run_etl:
	docker-compose up --build --remove-orphans --force-recreate -d
	docker-compose run --rm $(IMAGE_NAME) \
		poetry run python main.py --input=input  --output=output/sample_task --task=sample
