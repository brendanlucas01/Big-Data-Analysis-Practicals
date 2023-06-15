import findspark
findspark.init()
findspark.find()
import pyspark
findspark.find()
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
conf = pyspark.SparkConf().setAppName('appName').setMaster('local')
sc = pyspark.SparkContext(conf=conf)
spark = SparkSession(sc)


spark2 = SparkSession.builder.getOrCreate()

nums = sc.textFile("list.txt")
nums.collect()

counts = nums.flatMap(lambda x: x.split(' ')).map(lambda x: (int(x),1)).sortByKey()
output = counts.collect()
print()
print()

for (word,count) in output:
	print(word,end=", " )
print()
