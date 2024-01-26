import csv

def extract_data(file_name):
    """
    In this function, you should receive data with using native Python from below CSV files.
    Data is in CSV file format and you should append every record to a list. This list will
    be your raw data and you will use it in initial load to mongodb and for daily load
    to mongoDb.

    WLD_2023_SYNTH-SVY-HLD-EN_v01_M.csv
    WLD_2023_SYNTH-SVY-IND-EN_v01_M.csv


    Example
    -------
    :input:
    file_name

    :output:
    data_list

    :return: list of individual and household data in different lists
    """
    data_list = []

    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data_list.append(row)

    return data_list