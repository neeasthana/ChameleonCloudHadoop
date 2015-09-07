#ACX cluster single node pyspark installation documentation

##Launch single Ubuntu 14.04 Instance and ssh into it
```
ssh -i [$YOUR_KEY].pem ubuntu@[$YOUR_IP]
```


###Docker installation and image pull
Download Docker using command:
```
wget -qO- https://get.docker.com/ | sh
```

Make sure Docker is running using the command:
```
sudo docker run hello-world
```

Pull docker image using
```
sudo docker pull logbase/spark-ipython
```


###Launch a docker container
Launch the docker container and have the host listen on port 8888 using:
```
sudo docker run -i -t -p 127.0.0.1:8888:8888 logbase/spark-ipython /bin/bash
```


###Set password for iPython
Start ipython by using the command:
```
ipython
```

Import the library using:
```
from IPython.lib import passwd
```

Type this command and enter and confirm a password
```
passwd()
```
My configuration (ignore this):
```
	-password: neerajlcdm
	-sha1:a2c09a07de95:3bf56300860045d0e8127d858014413b461b7a1f
	sha1:d431fb3269da:db05f25d5164925da04d3b2390081b6ae2d21a93
```

Create the ipython server configuration files:
```
ipython profile create nbserver
```

Create a self signed certificate called pysparkipython.pem:
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout pysparkipython.pem -out pysparkipython.pem
```
	-answer all the questions provided or answer with '.'

Confirm that the certificate is there by running the directory command:
```
ls
```


###Configure the notebook server
Go into the directory containing the configuration file:
```
cd ~/.ipython/profile_nbserver/
```

Open configuration file in a text editor:
```
vi ipython_notebook_config.py
```

Add the following lines to this file after line 3:
```	
#Kernel Configuration
c.IPKernelApp.pylab = 'inline' # if you want plotting support always

#Notebook config
c.NotebookApp.certline = u'/home/pysparkipython.pem'
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha1:a2c09a07de95:3bf56300860045d0e8127d858014413b461b7a1f'
c.NotebookApp.port = 8888
```

Go into the startup folder and create a file named '00-pyspark-setup.py':
```
vi startup/00-pyspark-setup.py
```

Add these lines to the file:
```
	# Configure the necessary Spark environment
	import os
	import sys

	spark_home = os.environ.get('SPARK_HOME', None)
	sys.path.insert(0, spark_home + "/python")

	# Add the py4j to the path.
	# You may need to change the version number to match your install
	sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.8.2.1-src.zip'))

	# Initialize PySpark to predefine the SparkContext variable 'sc'
	execfile(os.path.join(spark_home, 'python/pyspark/shell.py'))
```


###Save the configuration
Commit your docker image:
```
sudo docker commit [$YOUR_CONTAINER_ID] ipython-server
```

This docker image can be launched using:
```
sudo docker run -i -t -p 8888:8888 ipython-server /bin/bash
```


###Start Hadoop services
Run bootstrap.sh to start hadoop services:
```
./etc/bootstrap.sh
```


###Start the server
Start the ipython server using the command:
```
nohup ipython notebook --profile=nbserver
```


###Stopping the server 
You can stop the server by finding the pid of the nohup.out file:
```
lsof nohup.out
```

Kill the proccess (PID) using:
```
kill -9 $PID
```