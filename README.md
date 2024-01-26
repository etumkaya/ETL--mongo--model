# Computational Data Science - Term Project

## About the Project 

This is our term project for our class MAT386E - Computational Data Science. Me and my colleagues, Konuralp Arslan and Ahmet Salih Çoşkun, worked together to finish and present it.
We used the "[Synthetic Data for an Imaginary Country, Sample, 2023 dataset](https://microdata.worldbank.org/index.php/catalog/5906/study-description)". The purpose of the project was to 
predict whether a family lives in a rural are or an urban one. We had two sample datasets. First one had the household data of 8000 families and numerous features whereas second one
had individual data for these families. We used the first one as our main dataset, and used the latter to merge and extract some features which can effect our model in a positive manner. 

We started our work with using PyCharm to do ETL to MongoDB. We utilised pyspark and pymongo. Then we read our saved data from Mongo in our Jupyter Notebook and performed cleaning,
transforming, feature extracting, visualizing. We merged the datasets, keeping the important features, and moved on to train machine learning models. We compared the metrics for our
models and saved the best one as a pickle file. For the last part of the work, we saved our predictions back to MongoDB. 

It was an end to end project which combined data engineering and data science tasks. It is also important to mention that we presented our work at the last week of this class. The presentation 
slides can also be found in this repository.

## About the Class

This is an elective course offered to Mathematical Engineering students in our school, ITU. The lecture is given by Machine Learning and Data Engineering professionals from Garanti 
BBVA Technology. From classification to deep learning; from Hadoop Environment to Spark ML, most of the key topics of big data, data engineering and data science are extensively taught and we were given 
many hands-on tasks. 
