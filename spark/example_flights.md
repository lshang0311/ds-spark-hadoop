
[Airline Flights Data](https://spark.rstudio.com/examples/yarn-cluster-emr/)


* airline carrier data
```bash
wget -O /tmp/airlines.csv http://www.transtats.bts.gov/Download_Lookup.asp?Lookup=L_UNIQUE_CARRIERS
```

```bash
hadoop@ubuntu:~$ hdfs dfs -mkdir /user/hadoop/airlines/
hadoop@ubuntu:~$ hdfs dfs -put /tmp/airlines.csv /user/hadoop/airlines
hadoop@ubuntu:~$ hdfs dfs -ls /user/hadoop/airlines
Found 1 items
-rw-r--r--   1 hadoop supergroup      50033 2018-08-23 18:42 /user/hadoop/airlines/airlines.csv
```

* Data - airlines

Hive - create table
```bash
hive> show tables;
OK
Time taken: 3.858 seconds
hive> CREATE EXTERNAL TABLE IF NOT EXISTS airlines
    > (
    > Code string,
    > Description string
    > )
    > ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
    > WITH SERDEPROPERTIES
    > (
    > "separatorChar" = '\,',
    > "quoteChar"     = '\"'
    > )
    > STORED AS TEXTFILE
    > tblproperties("skip.header.line.count"="1");
OK
Time taken: 0.427 seconds
```

Hive - load data to the table
```bash
hive> LOAD DATA INPATH '/user/hadoop/airlines' INTO TABLE airlines;
Loading data to table default.airlines
OK
Time taken: 0.656 seconds

hive> select * from airlines;
OK
02Q	Titan Airways
04Q	Tradewind Aviation
05Q	Comlux Aviation, AG
06Q	Master Top Linhas Aereas Ltd.
07Q	Flair Airlines Ltd
...
```

Spark shell - load csv file from hdfs
```bash
hadoop@ubuntu:~$ spark-shell --packages com.databricks:spark-csv_2.10:1.3.0
Spark context Web UI available at http://xxx.xxx.xx.xxx:4040
Spark context available as 'sc' (master = yarn, app id = application_1535009096477_0007).
Spark session available as 'spark'.
...
Using Scala version 2.11.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_181)
...

scala> 

# Check Spark UI on localhost:4040
```

```bash
scala> val sqlContext = new org.apache.spark.sql.SQLContext(sc)

# namenode adress: localhost:9000
scala> val input_df = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("delimiter",",").load("hdfs://localhost:9000/user/hadoop/airlines/airlines.csv")
    
scala> input_df.show(10)
+----+--------------------+
|Code|         Description|
+----+--------------------+
| 02Q|       Titan Airways|
| 04Q|  Tradewind Aviation|
| 05Q| Comlux Aviation, AG|
| 06Q|Master Top Linhas...|
| 07Q| Flair Airlines Ltd.|
| 09Q|Swift Air, LLC d/...|
| 0BQ|                 DCA|
| 0CQ|ACM AIR CHARTER GmbH|
| 0FQ|Maine Aviation Ai...|
| 0GQ|Inter Island Airw...|
+----+--------------------+
only showing top 10 rows
```
