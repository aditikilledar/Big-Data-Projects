from pyspark import SparkContext
from pyspark.sql import SQLContext
import sys

citypath=sys.argv[1]
globpath=sys.argv[2]

sc=SparkContext('local',"task2")
sqlContext = SQLContext(sc)

citydf = sqlContext.read.csv(citypath, header=True)
citydf = df.drop('AverageTemperatureUncertainty','Latitude','Longitude')

globdf = sqlContext.read.csv(globpath, header=True)

globdf = globdf.withColumn("LandAverageTemperature",globdf.LandAverageTemperature.cast('float'))
citydf = citydf.withColumn("AverageTemperature",citydf.AverageTemperature.cast('float'))

# globdf.show(20)