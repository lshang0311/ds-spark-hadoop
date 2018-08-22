# Apache Spark Clusters

```commandline
lshang@ubuntu:~$ export SPARK_HOME=/home/lshang/Downloads/spark-2.3.1-bin-hadoop2.7
lshang@ubuntu:~$ export set JAVA_OPTS="-Xmx9G -XX:MaxPermSize=2G -XX:+UseCompressedOops -XX:MaxMetaspaceSize=512m"
```
# Apache Spark Cluster - Running  a Spark Standalone Cluster
Master
```commandline
lshang@ubuntu:~/Downloads/spark-2.3.1-bin-hadoop2.7/sbin$ jps
17856 Jps

lshang@ubuntu:~/Downloads/spark-2.3.1-bin-hadoop2.7/sbin$ ./start-master.sh 
lshang@ubuntu:~/Downloads/spark-2.3.1-bin-hadoop2.7/sbin$ jps
17891 Master
17967 Jps
```

```commandline
lshang@ubuntu:~/Downloads/spark-2.3.1-bin-hadoop2.7/sbin$ cat /home/lshang/Downloads/spark-2.3.1-bin-hadoop2.7/logs/spark-lshang-org.apache.spark.deploy.master.Master-1-ubuntu.out
...
2018-08-19 14:24:26 INFO  Master:54 - I have been elected leader! New state: ALIVE
...
```

Spark UI
```buildoutcfg
http://localhost:8080/

URL: 
spark://ubuntu.localdomain:7077
```

Slave
```commandline
lshang@ubuntu:~/Downloads/spark-2.3.1-bin-hadoop2.7/sbin$ ./start-slave.sh spark://ubuntu.localdomain:7077

lshang@ubuntu:~/Downloads/spark-2.3.1-bin-hadoop2.7/sbin$ cat /home/lshang/Downloads/spark-2.3.1-bin-hadoop2.7/logs/spark-lshang-org.apache.spark.deploy.worker.Worker-1-ubuntu.out 
...
2018-08-19 21:43:39 INFO  Worker:54 - Successfully registered with master spark://ubuntu.localdomain:7077
```

```
lshang@ubuntu:~/Downloads/spark-2.3.1-bin-hadoop2.7/sbin$ jps
18071 Main
21975 Jps
21901 Worker
21789 Master

lshang@ubuntu:~/Downloads/spark-2.3.1-bin-hadoop2.7/bin$ ./spark-shell spark://ubuntu.localdomain:7077
scala> 
```

Find workers at
[localhost:8080](http://localhost:8080/)

