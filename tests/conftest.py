import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark_session(request):
    spark = (
        SparkSession.builder.appName("pytest-pyspark").master("local[2]").getOrCreate()
    )

    # Teardown code
    def teardown():
        spark.stop()

    # Register teardown code
    request.addfinalizer(teardown)

    return spark
