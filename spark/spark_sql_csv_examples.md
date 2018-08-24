
```bash
hadoop@ubuntu:~$ spark-shell --packages com.databricks:spark-csv_2.10:1.3.0

scala> val sqlContext = new org.apache.spark.sql.SQLContext(sc)
scala> val baby_names = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema", "true").load("file:///home/hadoop/baby_names.csv")
scala> baby_names.registerTempTable("names")
scala> val distinctYears = sqlContext.sql("select distinct Year from names")
distinctYears: org.apache.spark.sql.DataFrame = [Year: int]

scala> distinctYears.collect.foreach(println)
[2007]                                                                          
[2015]
[2013]
[2014]
[2012]
[2009]
[2016]
[2010]
[2011]
[2008]

scala> baby_names.printSchema
root
 |-- Year: integer (nullable = true)
 |-- First Name: string (nullable = true)
 |-- County: string (nullable = true)
 |-- Sex: string (nullable = true)
 |-- Count: integer (nullable = true)
```

Save to Hive
http://www.informit.com/articles/article.aspx?p=2756471&seqNum=5
TODO: rename header by remove space
```bash
scala> val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)
scala> baby_names.write.format("orc").saveAsTable("baby_names")
```
