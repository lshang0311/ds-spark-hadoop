# ds-spark-hadoop
Practical Data Science with Hadoop and Spark

Table of Contents
 * [Configuration](#configuration)
 * [Verify the Cluster Settings](#cluster-settings)
 * [Launch or stop Hadoop Cluster](#launch-hadoop-cluster)
 * [Report](#report)
 * [Spark](#spark)
 * [Examples](#examples)


# <a name="configuration"></a>Configuration
Installation guide:

[How to Setup Hadoop 3.1](https://tecadmin.net/setup-hadoop-single-node-cluster-on-centos-redhat/)

[Setup Hadoop 3.1.0 Single Node Cluster on Ubuntu 16.04](http://exabig.com/blog/2018/03/20/setup-hadoop-3-1-0-single-node-cluster-on-ubuntu-16-04/)

[Hadoop 3 Single-Node Install Guide](http://tech.marksblogg.com/hadoop-3-single-node-install-guide.html)

* Ubuntu Linux 16.04.1 - Master
     > 
       lshang@ubuntu:~$ hostname -I
       192.168.37.145
* Slaves
     >  slave01
        TODO


* Apache Hadoop 3.1.0
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

export HADOOP_HOME="/home/hadoop/hadoop-3.1.0"
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_MAPRED_HOME=${HADOOP_HOME}
export HADOOP_COMMON_HOME=${HADOOP_HOME}
export HADOOP_HDFS_HOME=${HADOOP_HOME}
export YARN_HOME=${HADOOP_HOME}
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

or
```
hadoop@ubuntu:~$ pdsh -q -w localhost
...
Rcmd type		ssh
...

export PDSH_RCMD_TYPE=ssh
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

[Cluster and Alll Applications](http://localhost:8042)

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

hadoop@ubuntu:~$ $HADOOP_HOME/bin/hadoop com.sun.tools.javac.Main


```
