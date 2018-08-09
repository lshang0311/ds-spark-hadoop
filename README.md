# ds-spark-hadoop
Practical Data Science with Hadoop and Spark

Configuration
========
* Ubuntu Linux 16.0.4 - Master
* Ubuntu Linux 16.0.4 - Slaves
* Apache Hadoop 2.7.3
* Apache Spark

Verify the Configuration of the MultiNode Hadoop 
===================
Master Node
-----------
Java 
```buildoutcfg
hadoop@ubuntu:~$ java -version
java version "1.8.0_181"
Java(TM) SE Runtime Environment (build 1.8.0_181-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.181-b13, mixed mode)

```

SSH
```buildoutcfg
hadoop@ubuntu:~$ ssh localhost
Welcome to Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-130-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

17 packages can be updated.
0 updates are security updates.

Last login: Thu Aug  9 04:22:31 2018 from 192.168.37.133
```

Node List
```
hadoop@ubuntu:/opt/hadoop/hadoop/sbin$ cat /opt/hadoop/hadoop/etc/hadoop/slaves 
192.168.37.135
192.168.37.134
```

Hadoop
```buildoutcfg
hadoop@ubuntu:~$ hadoop version
Hadoop 2.7.3
```

```buildoutcfg
hadoop@ubuntu:~$ cat ~/.bashrc 
...

export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
hadoop@ubuntu:~$ 

```

```
hadoop@ubuntu:~$ source ~/.bashrc 
hadoop@ubuntu:~$ echo $HADOOP_HOME 
/opt/hadoop/hadoop
```

Services in the Browser

[NameNode](http://192.168.37.134:50070/dfshealth.html#tab-overview)

Launch Hadoop Cluster
=====================

```buildoutcfg
lshang@ubuntu:~$ su - hadoop
Password: 
hadoop@ubuntu:~$ 
```

```buildoutcfg
hadoop@ubuntu:/opt/hadoop/hadoop/sbin$ jps
15410 Jps
hadoop@ubuntu:/opt/hadoop/hadoop/sbin$ start-dfs.sh
18/08/09 20:03:40 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Starting namenodes on [master]
master: starting namenode, logging to /opt/hadoop/hadoop/logs/hadoop-hadoop-namenode-ubuntu.out
192.168.37.134: starting datanode, logging to /opt/hadoop/hadoop/logs/hadoop-hadoop-datanode-ubuntu.out
192.168.37.135: starting datanode, logging to /opt/hadoop/hadoop/logs/hadoop-hadoop-datanode-ubuntu.out
Starting secondary namenodes [0.0.0.0]
0.0.0.0: starting secondarynamenode, logging to /opt/hadoop/hadoop/logs/hadoop-hadoop-secondarynamenode-ubuntu.out
18/08/09 20:03:58 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
hadoop@ubuntu:/opt/hadoop/hadoop/sbin$ jps
16054 Jps
15718 DataNode
15914 SecondaryNameNode
15566 NameNode

```



