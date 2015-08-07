#ACX cluster single node pyspark installation documentation

##Launch single Ubuntu 14.04 Instance and ssh into it
```
ssh -i [$YOUR_KEY].pem ubuntu@[$YOUR_IP]
```

###Docker installation and image pull
1. Download Docker using command:
```
wget -qO- https://get.docker.com/ | sh
```

2. Make sure Docker is running using the command:
```
sudo docker run hello-world
```

3. Pull docker image using
```
sudo docker pull logbase/spark-ipython
```

###Launch a docker container
1. Launch the docker container and have the host listen on port 8888 using:
```
sudo docker run -i -t -p 127.0.0.1:8888:8888 logbase/spark-ipython /bin/bash
```

###Set password for iPython
1. Start ipython by using the command:
```
ipython
```

2. Import the library using:
```
from IPython.lib import passwd
```

3. Type this command and enter and confirm a password
```
passwd()
```
	-neerajlcdm
	-sha1:a2c09a07de95:3bf56300860045d0e8127d858014413b461b7a1f
	sha1:d431fb3269da:db05f25d5164925da04d3b2390081b6ae2d21a93

4. Create the ipython server configuration files:
```
ipython profile create nbserver
```

5. Create a self signed certificate called pysparkipython.pem:
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout pysparkipython.pem -out pysparkipython.pem
```
	-answer all the questions provided or answer with '.'

6. Confirm that the certificate is there by running the directory command:
```
ls
```

###Configure the notebook server
1. Go into the directory containing the configuration file:
```
cd ~/.ipython/profile_nbserver/
```

2. Open configuration file in a text editor:
```
vi ipython_notebook_config.py
```

3. Add the following lines to this file after line 3:
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

4. Go into the startup folder and create a file named '00-pyspark-setup.py':
```
vi startup/00-pyspark-setup.py
```

5. Add these lines to the file:
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
1. Commit your docker image:
```
sudo docker commit <container_id> ipython-server
```

2. This docker image can be launched using:
```
sudo docker run -i -t -p 8888:8888 ipython-server /bin/bash
```

###Start Hadoop services
1. Run bootstrap.sh to start hadoop services:
```
./etc/bootstrap.sh
```

###Start the server
1. Start the ipython server using the command:
```
nohup ipython notebook --profile=nbserver
```

###Stopping the server 
1. You can stop the server by finding the pid of the nohup.out file:
```
lsof nohup.out
```

2. Kill the proccess (PID) using:
```
kill -9 $PID
```