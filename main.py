import argparse

from pyspark.sql import SparkSession

from assessment.task1.recipes_etl import RecipesETL
from assessment.task2.cook_time_etl import CookTimeETL

if __name__ == "__main__":

    # Argument Parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--task", type=str, required=True)

    args = parser.parse_args()

    input = args.input
    output = args.output
    task = args.task

    # Create a SparkSession
    spark = SparkSession.builder.getOrCreate()

    # Instantiate ETLs
    if task == "task1":
        etl = RecipesETL(input=input, output=output, spark_session=spark)
    else:
        etl = CookTimeETL(input=input, output=output, spark_session=spark)

    # Run ETL
    etl.run()

    print("INFO - ETL Done!")
