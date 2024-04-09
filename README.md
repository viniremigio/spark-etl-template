# Spark ETL instructions

This project bootstraps a template to create toy Spark ETL. This is useful to start a Spark project from scratch.


## Requirements
- This code was implemented using Python 3.10.14.
- You also need to install [Poetry](https://python-poetry.org/) as dependency management tool
- Run `poetry install` to install dependencies into a Poetry environment.

If you need to change some library version from *pyproject.toml*, run `poetry lock`.

Then run `poetry env info -p` to make sure the environment setup was done properly.


## Commands

- `make format_code`: rewrites source code using *black* and *isort* to keep it in the standard format
- `make lint`: checks the source code for syntax violations
- `make task1`: runs the ETL for task1. The output is located in *output/recipes* folder
- `make task2`: runs the ETL for task2. The output is located on *output/cook_time_difficulty* folder


## Sample structure

- The RecipesETL task comprises four methods inherited from the ETL superclass:
  - `extract()`: Read JSON files with recipes data
  - `transform()`: apply a lowercase function to the ingredients' column. This method also creates *year* and *month* columns, used for partitioning
  - `load()`: save transformed data to parquet files in partitioned folders
  - `run()`: call ETL methods in the correct order


## TODOs
- Finish docker setup
- Run a simple transformation
- Update documentation
- Logging setup
- Unit tests

## Documentation
- Further documentation can be placed in the [docs](docs/) folder.
