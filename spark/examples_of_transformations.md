# Apache Spark: Example of Transformations

```commandline
lshang@ubuntu:~$ wget -O ~/Downloads/baby_names.csv https://health.data.ny.gov/api/views/jxy9-yhdk/rows.csv?accessType=DOWNLOAD

lshang@ubuntu:~$ ls ~/Downloads/ba* -lart
-rw-rw-r-- 1 lshang lshang 5657962 Aug 17 22:46 /home/lshang/Downloads/babyNames.csv
```

```commandline
lshang@ubuntu:~$ export SPARK_HOME=/home/lshang/Downloads/spark-2.3.1-bin-hadoop2.7
lshang@ubuntu:~$ export set JAVA_OPTS="-Xmx9G -XX:MaxPermSize=2G -XX:+UseCompressedOops -XX:MaxMetaspaceSize=512m"
lshang@ubuntu:~$ spark-shell
```
Show header
```commandline
scala> val babyNames = sc.textFile("/home/lshang/Downloads/baby_names.csv")
babyNames: org.apache.spark.rdd.RDD[String] = /home/lshang/Downloads/baby_names.csv MapPartitionsRDD[1] at textFile at <console>:24

scala> val filteredRows=babyNames.filter(line => line.contains("Count"))
filteredRows: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[2] at filter at <console>:25

scala> filteredRows.foreach(println)
Year,First Name,County,Sex,Count
```

# Apache Spark: Example of Actions 
```commandline
scala> val names1 = sc.parallelize(List("abe", "abby", "apple"))
names1: org.apache.spark.rdd.RDD[String] = ParallelCollectionRDD[2] at parallelize at <console>:24

scala> names1.foreach(println)
abby
apple
abe

scala> names1.reduce((t1,t2) => t1 + ',' +  t2)
res2: String = abe,apple,abby
```
