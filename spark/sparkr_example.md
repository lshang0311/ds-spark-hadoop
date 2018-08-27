[Start Spark clusters](https://github.com/lshang0311/ds-spark-hadoop/blob/master/spark/spark_clusters.md)
```commandline
hadoop@ubuntu:~$ jps
24412 Jps

hadoop@ubuntu:~$ start-yarn.sh
hadoop@ubuntu:~$ start-dfs.sh

hadoop@ubuntu:~$ $SPARK_HOME/sbin/start-master.sh 
hadoop@ubuntu:~$ $SPARK_HOME/sbin/start-slave.sh spark://ubuntu:7077

hadoop@ubuntu:~$ jps
25376 DataNode
25792 Master
25906 Worker
25235 NameNode
24692 NodeManager
26005 Jps
24537 ResourceManager
25629 SecondaryNameNode
```

[Start RStudio Server](https://github.com/lshang0311/ds-spark-hadoop/blob/master/spark/install_sparklyr_on_ubuntu.md)
```commandline
lshang@ubuntu:~$ sudo /usr/sbin/rstudio-server stop
lshang@ubuntu:~$ sudo /usr/sbin/rstudio-server start
```

Launch RStudio from localhost:8787 and  install SparkR
```buildoutcfg
install.packages("https://cran.r-project.org/src/contrib/Archive/SparkR/SparkR_2.3.0.tar.gz", repos = NULL, type="source")
```

SparkR example: 
```markdown
Sys.setenv(HADOOP_CONF_DIR='/home/hadoop/hadoop/etc/hadoop')
Sys.setenv(YARN_CONF_DIR='/home/hadoop/hadoop-3.1.1/etc/hadoop')

Sys.setenv(SPARK_HOME = "/home/hadoop/spark")
library(SparkR, lib.loc = c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib")))

sparkR.session(master = "spark://ubuntu:7077", sparkHome = '/home/hadoop/spark', enableHiveSupport = FALSE)

faithful_df_spark <- SparkR::as.DataFrame(faithful)
head(faithful_df_spark)

df <- as.DataFrame(iris)
model <- glm(Sepal_Length ~  Sepal_Width + Species, data = df, family = "gaussianm")

summary(model)

predictions <- predict(model, newData = df)
head(select(predictions, "Sepal_Length", "prediction"))
```
