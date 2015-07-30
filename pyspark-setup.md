#ACX cluster single node pyspark installation documentation

##Launch single Ubuntu 14.04 Instance and ssh into it

###Docker installation and image pull
1. Download Docker using command:

2. Make sure Docker is running using the command:

3. Pull docker image using
	-sudo docker pull logbase/spark-ipython

###Launch a docker container
1. Launch the docker container and have the host listen on port 8888 using:
	-sudo docker run -i -t -p 127.0.0.1:8888:8888 logbase/spark-ipython /bin/bash

###Set password for iPython
1. Start ipython by using the command:
	-ipython

2. Import the library using:
	-from IPython.lib import passwd

3. Type this command and enter and confirm a password
	-passwd()
	-neerajlcdm
	-sha1:a2c09a07de95:3bf56300860045d0e8127d858014413b461b7a1f

4. Create the ipython server configuration files
	-ipython profile create nbserver

5. Create a self signed certificate called pysparkipython.pem
	-sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout pysparkipython.pem -out pysparkipython.pem
	-answer all the questions provided or answer with '.'

6. Confirm that the certificate is there by running the directory command
	-ls

###Configure the notebook server
1. Go into the directory containing the configuration file
	-cd ~/.ipython/profile_nbserver/

2. Open configuration file in a text editor
	-vi ipython_notebook_config.py

3. Add the following lines to this file after line 3
	-#Kernel Configuration
	c.IPKernelApp.pylab = 'inline' # if you want plotting support always

	#Notebook config
	c.NotebookApp.certline = u'/home/pysparkipython.pem'
	c.NotebookApp.ip = '*'
	c.NotebookApp.open_browser = False
	c.NotebookApp.password = u'sha1:a2c09a07de95:3bf56300860045d0e8127d858014413b461b7a1f'
	c.NotebookApp.port = 8888

###Start the server
1. Start the ipython server using the command:
	-ipython notebook --profile=nbserver