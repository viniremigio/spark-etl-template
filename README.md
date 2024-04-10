# Spark ETL instructions

This project bootstraps a template to create toy Spark ETL. This is useful to start a Spark project from scratch.


## Requirements
- Docker
- Python > 3.10
- [Poetry](https://python-poetry.org/) as dependency management tool. If you need to change some library version from *pyproject.toml*, run `poetry lock`.

Then run `poetry env info -p` to make sure the environment setup was done properly.


## Commands
- `make format_code`: rewrites source code using *black* and *isort* to keep it in the standard format
- `make lint`: checks the source code for syntax violations
- `make test`: Run unit tests 
- `make run_etl`: runs the ETL for the [sample_etl](src/sample_task/sample_etl.py). The output data will be located in the *output/sample* folder


## Sample structure
- The RecipesETL task comprises four methods inherited from the ETL superclass:
  - `extract()`: Read JSON files with recipes data
  - `transform()`: apply a lowercase function to the ingredients' column. This method also creates *year* and *month* columns, used for partitioning
  - `load()`: save transformed data to parquet files in partitioned folders
  - `run()`: call ETL methods in the correct order

## Documentation
- Further documentation can be placed in the [docs](docs/) folder.
