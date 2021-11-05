from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import col
import sys

# config
sc=SparkContext('local',"task2")
sqlContext = SQLContext(sc)

# args
citypath=sys.argv[1]
globpath=sys.argv[2]

# load dfs
citydf = sqlContext.read.csv(citypath, header=True)
globdf = sqlContext.read.csv(globpath, header=True)

# drop unwanted cols
globdf = globdf.drop('LandAverageTemperatureUncertainty','LandMaxTemperature','LandMaxTemperatureUncertainty','LandMinTemperature','LandMinTemperatureUncertainty','LandAndOceanAverageTemperature','LandAndOceanAverageTemperatureUncertainty')
citydf =  citydf.drop('AverageTemperatureUncertainty','Latitude','Longitude')

# typecasting
globdf =  globdf.withColumn("LandAverageTemperature",globdf.LandAverageTemperature.cast('float'))
citydf =  citydf.withColumn("AverageTemperature",citydf.AverageTemperature.cast('float'))

#grouping, rename col for joins
cityref=citydf.groupby('dt','Country').max('AverageTemperature')
globdf = globdf.withColumnRenamed('dt', 'globdt')

# join and aggregate with max
cityref=cityref.join(globdf,cityref.dt==globdf.globdt)
cityref=cityref.drop('globdt')
cityref=cityref.withColumnRenamed("max(AverageTemperature)","MAXTEMP")

# filter
cityref=cityref.filter(cityref.LandAverageTemperature < cityref.MAXTEMP)
#cityref.show(20)
#cityref=cityref.sort('Country')
#cityref.show(20)
#cityref=cityref.orderBy('dt','Country')
  
# mapreduce
rdd1 = cityref.rdd
rdd1=rdd1.map(lambda x: (x.Country,1))
rdd2=rdd1.reduceByKey(lambda a,b: a+b)
#rdd2.take(20)
rddc=rdd2.collect()
rddc=sorted(rddc,key=lambda x: x[0])
#print(rddc)

#rdd3 = rdd2.sortByKey()
for element in rddc:
    print(element[0], '\t', element[1])

#cityref.show(20)
#globdf.show(20)
#citydf.show()







