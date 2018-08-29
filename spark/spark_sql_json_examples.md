[spark sql tutorial](https://www.edureka.co/blog/spark-sql-tutorial/)

```commandline
hadoop@ubuntu:~$ spark-shell --packages com.databricks:spark-csv_2.10:1.3.0
...
Spark context available as 'sc' (master = yarn, app id = application_1535359374814_0001).
Spark session available as 'spark'.
...
```

```commandline
scala> val dataset = Seq((0, "hello"), (1, "world")).toDF("id", "text")

scala> val upper: String => String =_.toUpperCase
scala> import org.apache.spark.sql.functions.udf
scala> val upperUDF = udf(upper)

scala> dataset.withColumn("upper", upperUDF('text)).show
+---+-----+-----+
| id| text|upper|
+---+-----+-----+
|  0|hello|HELLO|
|  1|world|WORLD|
+---+-----+-----+

scala> spark.udf.register("myUpper", (input:String) => input.toUpperCase)
scala> spark.catalog.listFunctions.filter('name like "%upper%").show(false)
+-----+--------+-----------+-----------------------------------------------+-----------+
|name |database|description|className                                      |isTemporary|
+-----+--------+-----------+-----------------------------------------------+-----------+
|upper|null    |null       |org.apache.spark.sql.catalyst.expressions.Upper|true       |
+-----+--------+-----------+-----------------------------------------------+-----------+

scala> spark
res5: org.apache.spark.sql.SparkSession = org.apache.spark.sql.SparkSession@1bfac893

scala> import spark.implicits._

scala> val df = spark.read.json("file:///home/hadoop/spark/examples/src/main/resources/employees.json")
df: org.apache.spark.sql.DataFrame = [name: string, salary: bigint]             

scala> df.show()
+-------+------+                                                                
|   name|salary|
+-------+------+
|Michael|  3000|
|   Andy|  4500|
| Justin|  3500|
|  Berta|  4000|
+-------+------+

scala> df.printSchema()
root
 |-- name: string (nullable = true)
 |-- salary: long (nullable = true)


scala> df.select("name").show()
+-------+
|   name|
+-------+
|Michael|
|   Andy|
| Justin|
|  Berta|
+-------+
```

```commandline
scala> df.groupBy("name").count.show()
+-------+-----+                                                                 
|   name|count|
+-------+-----+
|Michael|    1|
|   Andy|    1|
|  Berta|    1|
| Justin|    1|
+-------+-----+

scala> df.createOrReplaceTempView("employee")
scala> val sqlDF = spark.sql("SELECT * FROM employee")
scala> sqlDF.show()
+-------+------+
|   name|salary|
+-------+------+
|Michael|  3000|
|   Andy|  4500|
| Justin|  3500|
|  Berta|  4000|
+-------+------+
```

sql details
```markdown
http://localhost:8088/cluster
   |
   -> http://localhost:8088/cluster/app/application_{id}
      |
      -> Tracking URL 
         |
         -> SQL
```

#TODO:
[Hive Tables - spark sql tutorial](https://www.edureka.co/blog/spark-sql-tutorial/)
