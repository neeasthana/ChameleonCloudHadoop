#ACX cluster single node pyspark with ipython installation documentation

followed kuntalganguly.com/2015/06/configure-ipython-notebook-with-apache.html
followed https://www.youtube.com/watch?v=q4PrYQOShnE
followed http://abisen.com/spark-from-ipython-notebook.html
followed ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/

##Launch single Ubuntu 14.04 Instance and ssh into it
```
ssh -i [$YOUR_KEY].pem ubuntu@[$YOUR_IP]
```



##Configure the system and download ipython
###Update the Ubuntu system
```
sudo apt-get update
```

###Install the packages for PIP and ipython-notebook
```
sudo apt-get install python-pip ipython-notebook
```

###Upgrade tornado
```
sudo pip install --upgrade ipython tornado
```

###Download ipython
```
sudo pip install ipython==3.2.1
```

###Download dependencies
```
sudo pip install jsonschema terminado
```

###Create notebooks directory
```
mkdir notebooks
```


##Configure Ipython profile

###Make a new ipython profile
```
ipython profile create nbserver
```

###Might need this to run ipython command
```
sudo pip install -I path.py==7.7.1
```
-password: neerajlcdm
-sha1:b312eea4d44b:b0d3d45b28ae79725484e2cbb162d4e18b16f0cb




##Download Spark
###Installing sbt
1.
```
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
```

2.
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823
```

3. Update ubuntu system
```
sudo apt-get update
```

4.Download SBT
```
sudo apt-get install sbt
```

###Install java jdk
```
sudo apt-get install default-jdk
```

###Set the hostname in the /etc/hosts

###Download and Install Spark
1.Retreive the .tgz file for spark installation
```
sudo wget http://d3kbcqa49mib13.cloudfront.net/spark-1.4.1-bin-hadoop2.6.tgz
```

2.Untar the file
```
tar -xvzf spark-1.4.1-bin-hadoop2.6.tgz
```

3.Go into the unzipped spark folder
```
cd spark-1.4.1-bin-hadoop2.6/
```

4.Assemble the program (may not be neccessary as it takes a long time)
```
sbt assembly
```

###Added SPARK_HOME and SUBMTI to .bashrc

###Added to .bashrc
```
export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
```

###Add Spark context to startup folder in nbserver profile and launch ipython server

Creating object for path '/org/freedesktop/NetworkManager/ActiveConnection/2' failed in libnm-glib.