from __future__ import annotations

from abc import ABC, abstractmethod

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType


class ETL(ABC):
    """
    ETL is an abstract class, based on Builder Pattern. Every class that extends from ETL will
    have extract, transform and load methods.
    """

    def __init__(self, input: str, output: str, spark_session: SparkSession):
        self.input = input
        self.output = output
        self.spark_session = spark_session
        self.df: DataFrame = spark_session.createDataFrame([], schema=StructType([]))

    @abstractmethod
    def extract(self) -> ETL:
        pass

    @abstractmethod
    def transform(self) -> ETL:
        pass

    @abstractmethod
    def load(self) -> ETL:
        pass

    def run(self) -> None:
        """
        Call ETL methods in the correct sequence
        :return: None
        """
        self.extract().transform().load()
