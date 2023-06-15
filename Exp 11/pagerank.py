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




# Adjacency list
links = sc.textFile('links.txt')
links.collect()


# Key/value pairs
links = links.map(lambda x: (x.split(' ')[0], x.split(' ')[1:]))
print(links.collect())
 
# Find node count
N = links.count()
print(N)

# Create and initialize the ranks
ranks = links.map(lambda node: (node[0],1.0/N))
print(ranks.collect())


ITERATIONS=20
for i in range(ITERATIONS):
    # Join graph info with rank info and propogate to all neighbors rank scores (rank/(number of neighbors)
    # And add up ranks from all in-coming edges
    ranks = links.join(ranks).flatMap(lambda x : [(i, float(x[1][1])/len(x[1][0])) for i in x[1][0]])\
    .reduceByKey(lambda x,y: x+y)
    print(ranks.sortByKey().collect())