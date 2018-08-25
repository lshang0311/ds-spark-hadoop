# Apache Spark Clusters

```commandline
hadoop@ubuntu:~$ echo $SPARK_HOME 
/home/hadoop/spark

lshang@ubuntu:~$ export SPARK_HOME=/home/lshang/Downloads/spark-2.3.1-bin-hadoop2.7
lshang@ubuntu:~$ export set JAVA_OPTS="-Xmx9G -XX:MaxPermSize=2G -XX:+UseCompressedOops -XX:MaxMetaspaceSize=512m"
```
# Apache Spark Cluster - Running  a Spark Standalone Cluster
Master
```commandline
hadoop@ubuntu:~$ $SPARK_HOME/sbin/start-master.sh 
starting org.apache.spark.deploy.master.Master, logging to /home/hadoop/spark/logs/spark-hadoop-org.apache.spark.deploy.master.Master-1-ubuntu.out
hadoop@ubuntu:~$ jps
6465 Jps
6403 Master
```

```commandline
hadoop@ubuntu:~$ cat $SPARK_HOME/logs/spark-hadoop-org.apache.spark.deploy.master.Master-1-ubuntu.out
========================================
2018-08-25 11:02:14 INFO  Utils:54 - Successfully started service 'sparkMaster' on port 7077.
2018-08-25 11:02:14 INFO  Master:54 - Starting Spark master at spark://ubuntu:7077
...
2018-08-25 11:02:14 INFO  Utils:54 - Successfully started service 'MasterUI' on port 8080.
...
2018-08-25 11:02:14 INFO  Master:54 - I have been elected leader! New state: ALIVE
...
```

```buildoutcfg
Find the 'sparkMaster' URL from 'MasterUI' (http://localhost:8080/)
or from the log ($SPARK_HOME/logs/spark-hadoop-org.apache.spark.deploy.master.Master-1-ubuntu.out):

spark://ubuntu:7077
```

Slave
```commandline
hadoop@ubuntu:~$ jps
6403 Master
6707 Jps

hadoop@ubuntu:~$ $SPARK_HOME/sbin/start-slave.sh spark://ubuntu:7077 
starting org.apache.spark.deploy.worker.Worker, logging to /home/hadoop/spark/logs/spark-hadoop-org.apache.spark.deploy.worker.Worker-1-ubuntu.out
hadoop@ubuntu:~$ jps
6849 Jps
6403 Master
6790 Worker

hadoop@ubuntu:~$ cat $SPARK_HOME/logs/spark-hadoop-org.apache.spark.deploy.worker.Worker-1-ubuntu.out
Spark Command: /usr/lib/jvm/java-8-oracle/bin/java -cp /home/hadoop/spark/conf/:/home/hadoop/spark/jars/*:/home/hadoop/hadoop/etc/hadoop/:/home/hadoop/hadoop-3.1.1/etc/hadoop/ -Xmx1g org.apache.spark.deploy.worker.Worker --webui-port 8081 spark://ubuntu:7077
========================================
2018-08-25 11:12:41 INFO  Worker:54 - Starting Spark worker xxx.xxx.xx.xxx:34111 with 4 cores, 6.8 GB RAM
2018-08-25 11:12:41 INFO  Utils:54 - Successfully started service 'WorkerUI' on port 8081.

2018-08-25 11:12:41 INFO  Worker:54 - Connecting to master ubuntu:7077...
...
2018-08-25 11:12:41 INFO  Worker:54 - Successfully registered with master spark://ubuntu:7077
```

Find workers at
[localhost:8080](http://localhost:8080/)

Connect REPL to SPark Cluster
```bash
hadoop@ubuntu:~$ $SPARK_HOME/bin/spark-shell --master spark://ubuntu:7077
...
Spark context Web UI available at http://xxx.xxx.xx.xxx:4040
Spark context available as 'sc' (master = spark://ubuntu:7077, app id = app-20180825112436-0000).
Spark session available as 'spark'.
...
scala> 
```

Stop the Master and the Slave
```bash
hadoop@ubuntu:~$ jps
6403 Master
7780 Jps
6790 Worker

hadoop@ubuntu:~$ $SPARK_HOME/sbin/stop-master.sh 
hadoop@ubuntu:~$ jps
6790 Worker
7817 Jps

hadoop@ubuntu:~$ $SPARK_HOME/sbin/stop-slave.sh 
hadoop@ubuntu:~$ jps
7843 Jps
```

