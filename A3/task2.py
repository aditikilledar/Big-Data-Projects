from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import col
import sys

sc=SparkContext('local',"task2")
sqlContext = SQLContext(sc)

citypath=sys.argv[1]
globpath=sys.argv[2]

citydf = sqlContext.read.csv(citypath, header=True)
globdf = sqlContext.read.csv(globpath, header=True)

#globdf = globdf.select(col('dt'),col('LandAverageTemperature'))
globdf = globdf.drop('LandAverageTemperatureUncertainty','LandMaxTemperature','LandMaxTemperatureUncertainty','LandMinTemperature','LandMinTemperatureUncertainty','LandAndOceanAverageTemperature','LandAndOceanAverageTemperatureUncertainty')

citydf =  citydf.drop('AverageTemperatureUncertainty','Latitude','Longitude')

globdf =  globdf.withColumn("LandAverageTemperature",globdf.LandAverageTemperature.cast('float'))
citydf =  citydf.withColumn("AverageTemperature",citydf.AverageTemperature.cast('float'))

cityref=citydf.groupby('dt','Country').max('AverageTemperature')
#cityref.show(20)

globdf = globdf.withColumnRenamed('dt', 'globdt')

cityref=cityref.join(globdf,cityref.dt==globdf.globdt)
cityref=cityref.drop('globdt')
cityref=cityref.withColumnRenamed("max(AverageTemperature)","MAXTEMP")
#cityref.show(5)
cityref=cityref.filter(cityref.LandAverageTemperature < cityref.MAXTEMP)
cityref=cityref.orderBy('dt','Country')
#cityref.show(20)
rdd1 = cityref.rdd
rdd1=rdd1.map(lambda x: (x.Country,1))
rdd2=rdd1.reduceByKey(lambda a,b: a+b)
rdd3 = rdd2.sortByKey()
for element in rdd3.collect():
    print(element[0], '\t', element[1])

#cityref.show(20)
#globdf.show(20)
#citydf.show(20)
