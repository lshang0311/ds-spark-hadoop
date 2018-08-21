# ds-spark-hadoop
Practical Data Science with Hadoop and Spark

Table of Contents
 * [Configuration](#configuration)
 * [Verify the Cluster Settings](#cluster-settings)
 * [Launch or stop Hadoop Cluster](#launch-hadoop-cluster)
 * [Report](#report)
 * [Spark](#spark)
 * [Hive](#hive)
 * [Examples](#examples)


# <a name="configuration"></a>Configuration
Installation guide:

[Setup Hadoop 3.1.0 Single Node Cluster on Ubuntu 16.04](http://exabig.com/blog/2018/03/20/setup-hadoop-3-1-0-single-node-cluster-on-ubuntu-16-04/)

also see:

[How to Setup Hadoop 3.1](https://tecadmin.net/setup-hadoop-single-node-cluster-on-centos-redhat/)

[Hadoop 3 Single-Node Install Guide](http://tech.marksblogg.com/hadoop-3-single-node-install-guide.html)

* Ubuntu Linux 16.04.1 - Master
     > 
       lshang@ubuntu:~$ hostname -I
       192.168.37.145
* Slaves
     >  slave01
        TODO


* Apache Hadoop 3.1.1
* Apache Spark

# <a name="cluster-settings"></a>Verify the Cluster Settings

Master Node
-----------
SSH
```buildoutcfg
Passwordless to Master
hadoop@ubuntu:~/hadoop/sbin$ ssh localhost
Welcome to Ubuntu 16.04.1 LTS (GNU/Linux 4.4.0-31-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

647 packages can be updated.
356 updates are security updates.

Last login: Fri Aug 10 10:27:34 2018 from 127.0.0.1
hadoop@ubuntu:~$ exit
logout
Connection to localhost closed.

```


bashrc
```buildoutcfg
hadoop@ubuntu:~$ cat ~/.bashrc 
...

export HADOOP_HOME=/home/hadoop/hadoop-3.1.1
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_MAPRED_HOME=${HADOOP_HOME}
export HADOOP_COMMON_HOME=${HADOOP_HOME}
export HADOOP_HDFS_HOME=${HADOOP_HOME}
export YARN_HOME=${HADOOP_HOME}
```

hadoop-env.sh
```
hadoop@ubuntu:~$ cat hadoop-3.1.1/etc/hadoop/hadoop-env.sh
...
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
...
```

core-site.xml
```buildoutcfg
hadoop@ubuntu:~$ cat /home/hadoop/hadoop-3.1.0/etc/hadoop/core-site.xml
<configuration>
 <property>
 <name>fs.defaultFS</name>
 <value>hdfs://localhost:9000</value>
 </property>
 <property>
 <name>hadoop.tmp.dir</name>
 <value>/home/hadoop/hdata</value>
 </property>
</configuration>
hadoop@ubuntu:~$
```

hdfs-site.xml
```buildoutcfg
hadoop@ubuntu:~$ cat /home/hadoop/hadoop-3.1.1/etc/hadoop/hdfs-site.xml 
<configuration>
<property>
 <name>dfs.replication</name>
 <value>1</value>
</property>

<property>
  <name>dfs.name.dir</name>
    <value>file:///home/hadoop/hadoopdata/hdfs/namenode</value>
</property>

<property>
  <name>dfs.data.dir</name>
    <value>file:///home/hadoop/hadoopdata/hdfs/datanode</value>
</property>
</configuration>
```

mapred-site.xml
```buildoutcfg
hadoop@ubuntu:~$ cat $HADOOP_HOME/etc/hadoop/mapred-site.xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>yarn.app.mapreduce.am.env</name>
        <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
    </property>
    <property>
        <name>mapreduce.map.env</name>
        <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
    </property>
    <property>
        <name>mapreduce.reduce.env</name>
        <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
    </property>
</configuration>
```

yarn-site.xml
```buildoutcfg
hadoop@ubuntu:~$ cat /home/hadoop/hadoop-3.1.1/etc/hadoop/yarn-site.xml 
<configuration>
 <property>
   <name>yarn.nodemanager.aux-services</name>
   <value>mapreduce_shuffle</value>
 </property>
 <property>
   <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
   <value>org.apache.hadoop.mapred.ShuffleHandler</value>
 </property>
</configuration>

```

Hadoop
```buildoutcfg
hadoop@ubuntu:~$ hadoop version
Hadoop 3.1.0
```


# <a name="launch-hadoop-cluster"></a>Launch or Stop Hadoop Cluster
On Master Node
```buildoutcfg
lshang@ubuntu:~$ su - hadoop
Password: 
hadoop@ubuntu:~$ 
```

```buildoutcfg
hadoop@ubuntu:~$ start-dfs.sh
```
To fix the permission denied error:

[Permission denied error while running start-dfs.sh](https://stackoverflow.com/questions/42756555/permission-denied-error-while-running-start-dfs-sh?rq=1)

```bash
echo "ssh" | sudo tee /etc/pdsh/rcmd_default
```

or 
```bash
hadoop@ubuntu:~$ pdsh -q -w localhost
...
Rcmd type		rsh
...
```

rsh -> ssh
```
hadoop@ubuntu:~$ export PDSH_RCMD_TYPE=ssh

hadoop@ubuntu:~$ pdsh -q -w localhost
...
Rcmd type		ssh
...

```

```
hadoop@ubuntu:~$ start-yarn.sh

hadoop@ubuntu:~$ jps
15250 SecondaryNameNode
17778 Jps
14870 NameNode
15833 NodeManager
15515 ResourceManager
15036 DataNode
```

```
hadoop@ubuntu:~$ stop-dfs.sh
Stopping namenodes on [localhost]
Stopping datanodes
Stopping secondary namenodes [ubuntu]
hadoop@ubuntu:~$ stop-yarn.sh
Stopping nodemanagers
Stopping resourcemanager
hadoop@ubuntu:~$ jps
18734 Jps
```

Services in the Browser

[NameNode](http://localhost:9870)

[Cluster and All Applications](http://localhost:8042)

[Hadoop Node Details](http://localhost:9864)


Logs
====
hadoop@ubuntu:~$ cat /home/hadoop/hadoop-3.1.0/logs/hadoop-hadoop-datanode-ubuntu.log

# <a name="report"></a>Report
```buildoutcfg
hadoop@ubuntu:~$ hadoop dfsadmin -report
Configured Capacity: 19945680896 (18.58 GB)
Present Capacity: 12856573952 (11.97 GB)
DFS Remaining: 12856524800 (11.97 GB)
DFS Used: 49152 (48 KB)
DFS Used%: 0.00%
Replicated Blocks:
	Under replicated blocks: 0
	Blocks with corrupt replicas: 0
	Missing blocks: 0
	Missing blocks (with replication factor 1): 0
	Pending deletion blocks: 0
Erasure Coded Block Groups:
	Low redundancy block groups: 0
	Block groups with corrupt internal blocks: 0
	Missing block groups: 0
	Pending deletion blocks: 0

-------------------------------------------------
Live datanodes (1):

Name: 127.0.0.1:9866 (localhost)
Hostname: ubuntu
Decommission Status : Normal
Configured Capacity: 19945680896 (18.58 GB)
DFS Used: 49152 (48 KB)
Non DFS Used: 6052327424 (5.64 GB)
DFS Remaining: 12856524800 (11.97 GB)
DFS Used%: 0.00%
DFS Remaining%: 64.46%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 1
Last contact: Fri Aug 10 19:21:39 PDT 2018
Last Block Report: Fri Aug 10 11:02:03 PDT 2018
Num of Blocks: 1
```

# <a name="spark"></a>Spark
```
export SPARK_HOME=/home/lshang/Downloads/spark-2.3.1-bin-hadoop2.7
export set JAVA_OPTS="-Xmx9G -XX:MaxPermSize=2G -XX:+UseCompressedOops -XX:MaxMetaspaceSize=512m"
$SPARK_HOME/bin/pyspark --packages databricks:spark-deep-learning:1.1.0-spark2.3-s_2.11 --driver-memory 5g
```
For more, see
[Spark Deep Learning](https://github.com/lshang0311/spark-deep-learning)

# <a name="hive"></a>Hive
See [Installing Hive on Ubuntu 16.04](https://hadoop7.wordpress.com/2017/01/27/installing-hive-on-ubuntu-16-04/)

```bash
lshang@ubuntu:~$ cd Downloads/
lshang@ubuntu:~/Downloads$ wget http://mirror.intergrid.com.au/apache/hive/hive-3.1.0/apache-hive-3.1.0-bin.tar.gz
lshang@ubuntu:~/Downloads$ tar -xzf apache-hive-3.1.0-bin.tar.gz 
lshang@ubuntu:~/Downloads$ sudo mv apache-hive-3.1.0-bin /usr/local/hive

lshang@ubuntu:~/Downloads$ vi ~/.bashrc 
lshang@ubuntu:~/Downloads$ su - hadoop
hadoop@ubuntu:~$ cd
hadoop@ubuntu:~$ vi .bashrc 
hadoop@ubuntu:~$ source ~/.bashrc 
hadoop@ubuntu:~$ echo $HIVE_HOME 
/usr/local/hive
hadoop@ubuntu:~$ exit
```

```bash
lshang@ubuntu:~/Downloads$ cd /usr/local/hive/
lshang@ubuntu:/usr/local/hive$ vi bin/hive-config.sh 
(add export HADOOP_HOME=/home/hadoop/hadoop-3.1.1)
```

```bash
lshang@ubuntu:/usr/local/hive/lib$ rm log4j-slf4j-impl-2.10.0.jar 
```

```bash
lshang@ubuntu:/usr/local/hive/lib$ cd
lshang@ubuntu:~$ su - hadoop
hadoop@ubuntu:~$ stop-all.sh 
hadoop@ubuntu:~$ jps
7259 Jps


hadoop@ubuntu:~$ start-dfs.sh
Starting namenodes on [localhost]
Starting datanodes
Starting secondary namenodes [ubuntu]

hadoop@ubuntu:~$ start-yarn.sh
hadoop@ubuntu:~$ jps
8592 Jps
7600 DataNode
7460 NameNode
8090 ResourceManager
7820 SecondaryNameNode
8223 NodeManager
```

```bash
hadoop@ubuntu:~$ hdfs dfs -mkdir -p /usr/hive/warehouse
hadoop@ubuntu:~$ hdfs dfs -chmod 777 /usr/hive/warehouse
```

```bash
hadoop@ubuntu:~$ schematool -initSchema -dbType derby
...
Initialization script completed
schemaTool completed
```

```bash
hadoop@ubuntu:~$ hive
Hive Session ID = cbcaa11a-a9ef-4112-bc09-29bffc066b97

Logging initialized using configuration in jar:file:/usr/local/hive/lib/hive-common-3.1.0.jar!/hive-log4j2.properties Async: true
Hive-on-MR is deprecated in Hive 2 and may not be available in the future versions. Consider using a different execution engine (i.e. spark, tez) or using Hive 1.X releases.
Hive Session ID = fccc52c5-a74c-4016-83d0-eacfe8e08618
hive> 
```

# <a name="examples"></a>Examples
Simple examples to get started.

* Put
```
hadoop@ubuntu:~$ hdfs dfs -mkdir /user/lshang
hadoop@ubuntu:~$ hdfs dfs -ls /user
Found 2 items
drwxr-xr-x   - hadoop supergroup          0 2018-08-11 05:08 /user/lshang
-rw-r--r--   1 hadoop supergroup         12 2018-08-10 10:54 /user/test.csv

hadoop@ubuntu:~$ hdfs dfs -put test.csv /user/lshang/test.csv
hadoop@ubuntu:~$ hdfs dfs -ls /user/lshang
Found 1 items
-rw-r--r--   1 hadoop supergroup         12 2018-08-11 05:09 /user/lshang/test.csv
```

* [Word counting by MapReduce](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
```
hadoop@ubuntu:~$ echo $JAVA_HOME
/usr/lib/jvm/java-8-oracle

hadoop@ubuntu:~$ export PATH=${JAVA_HOME}/bin:${PATH}
hadoop@ubuntu:~$ export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
```

```buildoutcfg
hadoop@ubuntu:~$ cat WordCount.java 
...
public class WordCount {

  public static class TokenizerMapper
  ...

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    ...
  }
}
```

```
hadoop@ubuntu:~$ $HADOOP_HOME/bin/hadoop com.sun.tools.javac.Main WordCount.java 
hadoop@ubuntu:~$ ls W* -lart
-rw-rw-r-- 1 hadoop hadoop 2092 Aug 11 05:51 WordCount.java
-rw-rw-r-- 1 hadoop hadoop 1736 Aug 11 05:53 WordCount$TokenizerMapper.class
-rw-rw-r-- 1 hadoop hadoop 1739 Aug 11 05:53 WordCount$IntSumReducer.class
-rw-rw-r-- 1 hadoop hadoop 1491 Aug 11 05:53 WordCount.class

hadoop@ubuntu:~$ jar cf wc.jar WordCount*.class
hadoop@ubuntu:~$ ls w*
wc.jar
```

```buildoutcfg
hadoop@ubuntu:~$ hdfs dfs -put file01.txt /user/lshang/wordcount/input/file01.txt
hadoop@ubuntu:~$ hdfs dfs -put file02.txt /user/lshang/wordcount/input/file01.txt

hadoop@ubuntu:~$ hdfs dfs -cat /user/lshang/wordcount/input/file01.txt
Hello World Bye World
hadoop@ubuntu:~$ hdfs dfs -cat /user/lshang/wordcount/input/file02.txt
Hello Hadoop goodbye Hadoop
```

```
hadoop@ubuntu:~$ hadoop jar wc.jar WordCount /user/lshang/wordcount/input /user/lshang/output
...
2018-08-11 07:32:29,364 INFO client.RMProxy: Connecting to ResourceManager at /0.0.0.0:8032
2018-08-11 07:32:36,880 INFO mapreduce.Job:  map 0% reduce 0%
2018-08-11 07:32:41,935 INFO mapreduce.Job:  map 100% reduce 0%
2018-08-11 07:32:47,979 INFO mapreduce.Job:  map 100% reduce 100%
2018-08-11 07:32:48,993 INFO mapreduce.Job: Job job_1533989259703_0010 completed successfully
2018-08-11 07:32:49,068 INFO mapreduce.Job: Counters: 53
...
```

```
hadoop@ubuntu:~$ hdfs dfs -ls  /user/lshang/output
Found 2 items
-rw-r--r--   1 hadoop supergroup          0 2018-08-11 07:32 /user/lshang/output/_SUCCESS
-rw-r--r--   1 hadoop supergroup         41 2018-08-11 07:32 /user/lshang/output/part-r-00000

hadoop@ubuntu:~$ hdfs dfs -cat  /user/lshang/output/part-r-00000
Bye	1
Hadoop	2
Hello	2
World	2
goodbye	1
```

* [Hadoop Streaming - find average flight delay](https://github.com/bbengfort/hadoop-fundamentals/tree/master/streaming)

Use pipe to test mapper and reducer
```
hadoop@ubuntu:~$ pwd
/home/hadoop
hadoop@ubuntu:~$ cat work.github/ds-spark-hadoop/mapreduce/flights.csv | ./work.github/ds-spark-hadoop/mapreduce/mapper.py | sort | ./work.github/ds-spark-hadoop/mapreduce/reducer.py 
JFK	3.0
LAX	6.0
```

Execute the job
```
hadoop@ubuntu:~/work.github/ds-spark-hadoop/mapreduce$ hdfs dfs -mkdir /user 
hadoop@ubuntu:~/work.github/ds-spark-hadoop/mapreduce$ hdfs dfs -mkdir /user/hadoop 
```

```
hadoop@ubuntu:~/work.github/ds-spark-hadoop/mapreduce$ ls flights.csv -lart
-rw-r--r-- 1 lshang lshang 321 Aug 12 20:26 flights.csv

hadoop@ubuntu:~/work.github/ds-spark-hadoop/mapreduce$ hdfs dfs -put flights.csv /user/hadoop/flights.csv
```

```
hadoop@ubuntu:~/work.github/ds-spark-hadoop/mapreduce$ hadoop jar /home/hadoop/hadoop-3.1.1/share/hadoop/tools/lib/hadoop-streaming-*.jar -input flights.csv -output average_delay -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py 
...
2018-08-14 22:06:49,676 INFO mapreduce.Job:  map 0% reduce 0%
2018-08-14 22:06:59,792 INFO mapreduce.Job:  map 100% reduce 0%
2018-08-14 22:07:03,821 INFO mapreduce.Job:  map 100% reduce 100%
2018-08-14 22:07:04,832 INFO mapreduce.Job: Job job_1534247413800_0002 completed successfully
2018-08-14 22:07:04,904 INFO mapreduce.Job: Counters: 54
...
2018-08-14 22:07:04,905 INFO streaming.StreamJob: Output directory: average_delay
```

```
hadoop@ubuntu:~/work.github/ds-spark-hadoop/mapreduce$ hdfs dfs -cat /user/hadoop/average_delay/part-00000
JFK	3.0
LAX	6.0
```

* spark-shell
```commandline
lshang@ubuntu:~$ pwd
/home/lshang

lshang@ubuntu:~$ wget -O ~/Downloads/baby_names.csv https://health.data.ny.gov/api/views/jxy9-yhdk/rows.csv?accessType=DOWNLOAD

lshang@ubuntu:~$ ls ~/Downloads/ba* -lart
-rw-rw-r-- 1 lshang lshang 5657962 Aug 17 22:46 /home/lshang/Downloads/babyNames.csv
```

```commandline
lshang@ubuntu:~$ export SPARK_HOME=/home/lshang/Downloads/spark-2.3.1-bin-hadoop2.7
lshang@ubuntu:~$ export set JAVA_OPTS="-Xmx9G -XX:MaxPermSize=2G -XX:+UseCompressedOops -XX:MaxMetaspaceSize=512m"
lshang@ubuntu:~$ spark-shell

scala> sc
res0: org.apache.spark.SparkContext = org.apache.spark.SparkContext@2a5c6b76

scala> val babyNames = sc.textFile("/home/lshang/Downloads/baby_names.csv")

scala> babyNames.count
res1: Long = 235511
```