from __future__ import annotations

from pyspark.sql.functions import col

from src.etl import ETL


class SampleETL(ETL):
    def extract(self) -> SampleETL:
        """
        The extract function reads CSV files and stores it into a DataFrame
        :return: SampleETL
        """
        schema = (
            self.spark_session.read.option("mergeSchema", "true")
            .option("header", "true")
            .csv(self.input)
            .schema
        )
        print(f"INFO -  Extract Step... Schema: {schema}")

        self.df = self.spark_session.read.csv(self.input, schema=schema)

        return self

    def transform(self) -> SampleETL:
        """
        The transform function into the original dataframe
        :return: SampleETL
        """
        print("INFO - Transformation Step")

        self.df = (
            self.df.filter(col("cyl") == 4)
            .withColumnRenamed("cyl", "cylinder")
            .select("model", "cylinder", "hp")
        )

        return self

    def load(self) -> SampleETL:
        """
        The load function persists transformed dataframe as JSON files.
        :return: SampleETL
        """
        print(f"INFO - Load Step: {self.output}")

        self.df.coalesce(1).write.mode("overwrite").json(path=self.output)

        return self
