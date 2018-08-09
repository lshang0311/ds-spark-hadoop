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

Hadoop
```buildoutcfg
hadoop@ubuntu:~$ hadoop version
Hadoop 2.7.3
```
