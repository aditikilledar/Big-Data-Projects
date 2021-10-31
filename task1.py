from pyspark import SparkContext
from pyspark.sql import SQLContext
import sys

country=sys.argv[1]
citycsv=sys.argv[2]

sc=SparkContext('local',"task1")
sqlContext = SQLContext(sc)


df=sqlContext.read.csv(citycsv, header=True)
df=df.drop('AverageTemperatureUncertainty','Latitude','Longitude')
df=df.withColumn("AverageTemperature",df.AverageTemperature.cast('float'))

df=df.filter(df.Country==country)
ref=df.groupby('City').mean('AverageTemperature')
ref.show(5)
#df=df.filter(df.AverageTemperature > ref[ref.City == df.City]['avg(AverageTemperature)']) 
df=df.join(ref,df.City==ref.City,'left')
df=df.withColumnRenamed("avg(AverageTemperature)","AVGTEMP")
df=df.filter(df.AverageTemperature > df.AVGTEMP)
df.show(20)
#df.select("AverageTemperature", df.AverageTemperature.like(f'{country}')).show(5)
