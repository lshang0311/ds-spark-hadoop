# Install RStudio Server

[Install the current version of RStudio server](https://www.rstudio.com/products/rstudio/download-server/)
```commandline
lshang@ubuntu:~$ sudo apt-get install -y gdebi-core
lshang@ubuntu:~$ wget https://download2.rstudio.org/rstudio-server-1.1.453-amd64.deb
lshang@ubuntu:~$ sudo gdebi rstudio-server-1.1.453-amd64.deb
...

● rstudio-server.service - RStudio Server
   Loaded: loaded (/etc/systemd/system/rstudio-server.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2018-08-20 21:57:55 AEST; 1s ago
  Process: 60847 ExecStart=/usr/lib/rstudio-server/bin/rserver (code=exited, status=0/SUCCESS)
 Main PID: 60851 (rserver)
    Tasks: 3
   Memory: 1.1M
      CPU: 474ms
   CGroup: /system.slice/rstudio-server.service
           └─60851 /usr/lib/rstudio-server/bin/rserver

Aug 20 21:57:55 ubuntu systemd[1]: Starting RStudio Server...
Aug 20 21:57:55 ubuntu systemd[1]: Started RStudio Server.
```

Stop the server
```commandline
lshang@ubuntu:~$ sudo /usr/sbin/rstudio-server stop
```

Restart the server
```commandline
lshang@ubuntu:~$ sudo /usr/sbin/rstudio-server restart
```

By default RStudio Server is running on 
[localhost:8787](localhost:8787)  

Use the user **hadoop** to login to the RStudio server or create a new user with a user name such as *rstudio**.

Create a user with user name **rstudio** and the home directory and password for it
```commandline
sudo useradd rstudio
sudo mkdir /home/rstudio
sudo passwd rstudio
sudo chmod -R 0777 /home/rstudio
```

login as **rstudio** or **hadoop**

```commandline
install.packages("sparklyr")
```
Also see the example [Using sparklyr with an Apache Spark cluster](https://spark.rstudio.com/examples/yarn-cluster-emr/) for the installation of *sparklyr*.

