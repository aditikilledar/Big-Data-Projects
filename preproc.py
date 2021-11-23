from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession, Row
from pyspark.sql import functions as F
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
#from textblob import TextBlob

sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

spark = SparkSession(sc)

def preprocessing(lines):
    words = lines.select(explode(split(lines.value, '",')).alias("word"))
    words = words.na.replace('', None)
    words = words.na.drop()
    words = words.withColumn('word', F.regexp_replace('word', r'http\S+', ''))
    words = words.withColumn('word', F.regexp_replace('word', '@\w+', ''))
    words = words.withColumn('word', F.regexp_replace('word', '#', ''))
    words = words.withColumn('word', F.regexp_replace('word', 'RT', ''))
    words = words.withColumn('word', F.regexp_replace('word', ':', ''))
    words = words.withColumn('word', F.regexp_replace('word', '",', ''))
    words = words.withColumn('word', F.regexp_replace('word', '\\n', ''))
    words = words.withColumn('Sen',words.word[0])
    return words

spark = SparkSession.builder.appName("TwitterSentimentAnalysis").getOrCreate()
# read the tweet data from socket
lines = spark.readStream.format("socket").option("host", "localhost").option("port", 6100).load()
BRO = preprocessing(lines)
# words = preprocessing(lines)
# Preprocess the data
query = BRO.writeStream.format('console').start()
query.awaitTermination()

