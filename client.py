'''
Om Arham Mukha Kamal Vaasinee Paapaatma Kshayam Kaari Vad Vad Vaagwaadinee Saraswati Aing Hreeng Namah Swaaha 
'''
from pyspark import SparkContext
from pyspark.streaming import StreamingContext, DStream
from pyspark.sql import SQLContext
import sys
from typing import Tuple


# config
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)
sqc = SQLContext(sc)

def line_to_tuple(line: str) -> Tuple[str, str]:
        try:
            k, v = line.split(",")
            return k, v
        except ValueError:
            return "", ""

def clean(x):
	x = x.replace('\\n', '')
	x = x.replace('\\', '')
	return x

def test(x):
	x.toDF().show()

lines = ssc.socketTextStream('localhost', 6100)
col_path = "./columns.csv"
line_tuple = ssc.sparkContext.textFile(col_path).map(line_to_tuple)
PLS = lines.flatMap(lambda line: line.split(','))
lines.transform(lambda rdd: test(rdd))
#lines.flatMap(lambda x: x.split(',')).foreachRDD(lambda x: test(x))
ltc = line_tuple.collect()
#PLS.pprint()
for i in ltc:
	print(i)
#line_tuple.toDF().show()
#rdd2 = line_tuple.flatMapValues(lambda x : [ (k, x[k]) for k in x.keys()])
#line_tuple.pprint()
#words = lines.map(lambda line: clean(line)).reduce(lambda x, y: x.join(y))
#words.transform(lambda x: x.take(20))
#words.pprint(20)

ssc.start()
ssc.awaitTermination()

