def load_data(ind_data, hld_data):
    """
    This function gets individual info dataframe and household info dataframe. It loads data to mongodb in separate collections
    but in the same database. You should be careful about the write mode and you can find the sample code in this url.
    https://docs.mongodb.com/spark-connector/current/python/write-to-mongodb/

    :param ind_data: Dataframe of Individual Data
    :param hld_data: Dataframe of Household Data
    """

    mongo_uri = "mongodb://127.0.0.1:27017"
    database_name = "COMP"
    ind_collection_name = "INDIVIDUAL"
    hld_collection_name = "HOUSEHOLD"

    ind_data.write.format("mongo").mode("overwrite").option("uri",mongo_uri + "/" + database_name + "." + ind_collection_name).save()

    hld_data.write.format("mongo").mode("overwrite").option("uri",mongo_uri + "/" + database_name + "." + hld_collection_name).save()
