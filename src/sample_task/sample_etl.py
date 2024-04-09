from __future__ import annotations

from pyspark.sql.functions import col, date_format, lower

from etl import ETL


class SampleETL(ETL):
    def extract(self) -> SampleETL:
        """
        The extract function for recipes reads JSON files and stores it into a DataFrame
        :return: SampleETL
        """
        schema = (
            self.spark_session.read.option("mergeSchema", "true")
            .json(self.input)
            .schema
        )
        print(f"INFO - Recipes schema: {schema}")
        self.df = self.spark_session.read.json(self.input, schema=schema)
        return self

    def transform(self) -> SampleETL:
        """
        The transform function for recipes perform transformations into the original dataframe
        :return: SampleETL
        """
        print("INFO - Perform transformations")
        self.df = (
            self.df.withColumn("ingredients", lower(col("ingredients")))
            .withColumn("year", date_format(col("datePublished"), format="yyyy"))
            .withColumn("month", date_format(col("datePublished"), format="MM"))
        )
        return self

    def load(self) -> SampleETL:
        """
        The load function for recipes persists transformed dataframe as parquet files.
        Partitioned by year and month
        :return: SampleETL
        """
        print(f"INFO - Saving into path: {self.output}")
        self.df.write.partitionBy("year", "month").mode("overwrite").parquet(
            path=self.output
        )
        return self
