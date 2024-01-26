from pyspark import SparkConf
from pyspark.sql import SparkSession
from extract import extract_data
from transformation import transform_data
from load import load_data


def get_spark_utils():
    """
    !!!DO NOT TOUCH!!!
    This function returns spark context object and spark session object.
    These are the entry point into all functionality in Spark.
    :return: SparkContext, SparkSession
    """
    conf = SparkConf().setAppName("Covid"). \
        set("spark.mongodb.input.uri", "mongodb://127.0.0.1"). \
        set("spark.mongodb.output.uri", "mongodb://127.0.0.1"). \
        set("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1"). \
        set("spark.sql.debug.maxToStringFields", 1000)
    spark = SparkSession.builder.master("local[*]").config(conf=conf).getOrCreate()
    sc = spark.sparkContext
    return sc, spark


if __name__ == '__main__':
    """
    This is your main function and this contains your flow.get_spark_utils function provide
    necessary variables for you like spark context.You should 
    call extract, transform?? and load functions respectively from their modules.
    
    Hint**: You may convert extracted data to RDD after that convert it to Dataframe.
    """
    sc, spark = get_spark_utils()

    Household_Extracted = extract_data("WLD_2023_SYNTH-SVY-HLD-EN_v01_M.csv")
    Household_Transformed = transform_data(spark, Household_Extracted)

    Individual_Extracted = extract_data('WLD_2023_SYNTH-SVY-IND-EN_v01_M.csv')
    Individual_Transformed = transform_data(spark, Individual_Extracted)

    load_data(Individual_Transformed, Household_Transformed)

    print("finish")
