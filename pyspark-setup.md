#ACX cluster single node pyspark installation documentation

##Launch single Ubuntu 14.04 Instance and ssh into it

##Install and Cogfiguring the Docker Container

###Docker installation and image pull

###Launch a docker container
1. Launch the docker container and expose port 8888 using:
	-sudo docker run -i -t -p 127.0.0.1:8888:8888 anaderi/docker-spark-ipython /bin/bash

###Install pip
1. Download get-pip.py:
	-sudo wget https://bootstrap.pypa.io/get-pip.py 

2. Run the script:
	-python get-pip.py

3.