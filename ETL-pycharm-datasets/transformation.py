from pyspark.sql import Row

def transform_data(spark, input_list):
    # Convert list of dictionaries to RDD of Rows
    rdd = spark.sparkContext.parallelize(input_list).map(lambda x: Row(**x))

    # Create PySpark DataFrame from RDD
    df = spark.createDataFrame(rdd)

    return df