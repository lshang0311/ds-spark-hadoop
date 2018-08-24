
[Airline Flights Analysis](https://spark.rstudio.com/examples/yarn-cluster-emr/)

[Getting Started with Apache Spark DataFrames in Python and Scala](http://www.sparktutorials.net/getting-started-with-apache-spark-dataframes-in-python-and-scala][DataFrames%20article]].%20We)

[Analyzing Flight Data: A Gentle Introduction to GraphX in Spark](http://www.sparktutorials.net/Analyzing+Flight+Data%3A+A+Gentle+Introduction+to+GraphX+in+Spark)

[Data Science with Hadoop - predicting airline delays](http://nbviewer.jupyter.org/github/ofermend/IPython-notebooks/blob/master/blog-part-1.ipynb)

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
     (
     Code string,
     Description string
     )
     ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
     WITH SERDEPROPERTIES
     (
     "separatorChar" = '\,',
     "quoteChar"     = '\"'
     )
     STORED AS TEXTFILE
     tblproperties("skip.header.line.count"="1");
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

```bash
hive> select count(*) from airlines;
...
1649
```

```bash
hive> desc formatted airlines;
OK
# col_name            	data_type           	comment             
	 	 
code                	string              	from deserializer   
description         	string              	from deserializer   
	 	 
# Detailed Table Information	 	 
Database:           	default             	 
Owner:              	hadoop              	 
CreateTime:         	Fri Aug 24 10:03:56 AEST 2018	 
LastAccessTime:     	UNKNOWN             	 
Retention:          	0                   	 
Location:           	hdfs://localhost:9000/user/hive/warehouse/airlines	 
Table Type:         	EXTERNAL_TABLE      	 
Table Parameters:	 	 
	COLUMN_STATS_ACCURATE	{\"COLUMN_STATS\":{\"code\":\"true\",\"description\":\"true\"}}
	EXTERNAL            	TRUE                
	numFiles            	2                   
	numRows             	0                   
	rawDataSize         	0                   
	skip.header.line.count	1                   
	totalSize           	100066              
	transient_lastDdlTime	1535069095          
	 	 
# Storage Information	 	 
SerDe Library:      	org.apache.hadoop.hive.serde2.OpenCSVSerde	 
InputFormat:        	org.apache.hadoop.mapred.TextInputFormat	 
OutputFormat:       	org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat	 
Compressed:         	No                  	 
Num Buckets:        	-1                  	 
Bucket Columns:     	[]                  	 
Sort Columns:       	[]                  	 
Storage Desc Params:	 	 
	quoteChar           	\"                  
	separatorChar       	,                   
	serialization.format	1                   
Time taken: 0.036 seconds, Fetched: 35 row(s)
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

Spark shell - load table from Hive 
```bash
scala> import org.apache.spark.sql.hive.HiveContext
scala> val sqlContext = new HiveContext(sc)

scala>  var db = sqlContext.sql("select * from airlines")
db: org.apache.spark.sql.DataFrame = [code: string, description: string]

scala> db.count()
res1: Long = 1650                                                               

scala> db.columns
res2: Array[String] = Array(code, description)
```

```bash
scala> sqlContext.sql("show databases")
res1: org.apache.spark.sql.DataFrame = [databaseName: string]

scala> sqlContext.sql("show databases").show()
+------------+
|databaseName|
+------------+
|     default|
+------------+

scala> sqlContext.sql("show tables").show()
+--------+---------+-----------+
|database|tableName|isTemporary|
+--------+---------+-----------+
| default| airlines|      false|
+--------+---------+-----------+
```

```bash
scala> val airlines = sqlContext.sql("select * from airlines")
scala> airlines.show(10)
+----+--------------------+
|code|         description|
+----+--------------------+
|Code|         Description|
| 02Q|       Titan Airways|
| 04Q|  Tradewind Aviation|
| 05Q| Comlux Aviation, AG|
| 06Q|Master Top Linhas...|
| 07Q| Flair Airlines Ltd.|
| 09Q|Swift Air, LLC d/...|
| 0BQ|                 DCA|
| 0CQ|ACM AIR CHARTER GmbH|
| 0FQ|Maine Aviation Ai...|
+----+--------------------+
only showing top 10 rows
```

```bash
scala> sqlContext.sql("select count(*) from airlines").show()
+--------+
|count(1)|
+--------+
|    1650|
+--------+
```