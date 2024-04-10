import pytest
from pyspark.sql.types import StringType, StructField, StructType
from pyspark.testing.utils import assertDataFrameEqual, assertSchemaEqual

from src.sample_task.sample_etl import SampleETL


@pytest.fixture
def expected_output():
    return [
        {"model": "Datsun 710", "cylinder": "4", "hp": "93"},
        {"model": "Merc 240D", "cylinder": "4", "hp": "62"},
        {"model": "Merc 230", "cylinder": "4", "hp": "95"},
        {"model": "Fiat 128", "cylinder": "4", "hp": "66"},
        {"model": "Honda Civic", "cylinder": "4", "hp": "52"},
        {"model": "Toyota Corolla", "cylinder": "4", "hp": "65"},
        {"model": "Toyota Corona", "cylinder": "4", "hp": "97"},
        {"model": "Fiat X1-9", "cylinder": "4", "hp": "66"},
        {"model": "Porsche 914-2", "cylinder": "4", "hp": "91"},
        {"model": "Lotus Europa", "cylinder": "4", "hp": "113"},
        {"model": "Volvo 142E", "cylinder": "4", "hp": "109"},
    ]


@pytest.fixture
def expected_output_schema():
    return StructType(
        [
            StructField("model", StringType(), nullable=False),
            StructField("cylinder", StringType(), nullable=False),
            StructField("hp", StringType(), nullable=False),
        ]
    )


def test_dataframe_is_equal(spark_session, expected_output, expected_output_schema):
    expected_df = spark_session.createDataFrame(
        expected_output, schema=expected_output_schema
    )

    etl = SampleETL(
        input="input/mtcars.csv",
        output="output/sample_task",
        spark_session=spark_session,
    )

    actual_df = etl.extract().transform().df
    assertSchemaEqual(actual=actual_df.schema, expected=expected_df.schema)
    assertDataFrameEqual(actual=actual_df, expected=expected_df)
