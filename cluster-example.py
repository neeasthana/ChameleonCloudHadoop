#Neeraj Asthana for LCDM group under Professor Robert Brunner
#University of Illinois at Urbana-Champaign
#Accessing PySpark Cluster from IPython notebook

#Initializes a proper Spark Context(sc)
#Will be included inside of a startup script so it will be not viewable to user
import os, sys

spark_home = os.environ.get('SPARK_HOME', None)
sys.path.insert(0, spark_home + "/python")

sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.8.2.1-src.zip'))

import pyspark
from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("spark://10.0.3.70:7077").setAppName("Testing Neeraj").set("spark.driver.port",8200)
sc = SparkContext(conf=conf)


#Ensure that there is an existing Spark context
sc

#Load text file from HDFS storage
text_file = sc.textFile('hdfs://10.0.3.113:9000/home/ubuntu/data/1987.csv')

text_file.take(10)

#Counting the number of elements in 1987.csv
text_file.count()

#Close the Spark Context to unallocate the resources
sc.stop()
sc