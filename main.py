import argparse

from pyspark.sql import SparkSession
from src.sample_task.sample_etl import SampleETL

if __name__ == "__main__":

    # Argument Parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--task", type=str, required=True, default="sample")

    args = parser.parse_args()

    input = args.input
    output = args.output
    task = args.task

    # Create a local SparkSession
    spark = SparkSession.builder.getOrCreate()

    # Instantiate ETL
    if task == "sample":
        etl = SampleETL(input=input, output=output, spark_session=spark)
        etl.run()
