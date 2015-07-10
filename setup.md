#Chameleon Cloud installation documentation

##Launch Instances

- Associate floating IP to the server

- change permissions of the .pem file using chmod command

- Note down local IP addresses of the server and the agents

##Configure Server (answer "y" to everything unless instructed not to)

###ssh configuration on server
1. Transfer ssh file using the scp command

2. cp .pem .shh/id_rsa

3. ssh into the server using ssh -X -i .pem cc@floatingIP

###NTPD
1. Install ntpd using: 
	-sudo yum install ntp ntpdate ntp-doc

2. Check to make sure ntpd is installed using
	-chkconfig --list ntpd 

3. Turn on ntpd
	-sudo chkconfig ntpd on

4. Start ntpd
	-sudo service ntpd start

###Configuring hostname and DNS
1. Set a hostname for the server, for example
	-sudo hostname master.hortonworks.cluster.com 

2. Make sure that the hostname is set using the hostname command (make it returns exactly what you set)

3. Navigate to the networks file using
	-sudo vi /etc/sysconfig/network

4. Change the value of hostname to the hostname for the server you just set

5. Open hosts file inside on a text editor with root privelidges
	-sudo vi /etc/hosts

6. DO NOT DELETE ANYTHING FROM THIS FILE! Add the line to include your local IP and associated hostname. For example
	-192.168.0.74   master.hortonworks.cluster.com

7. Add local IPs and hostnames for the agents. For example
	-

###Turn off the ip tables
1. Run command:
	-sudo chkconfig iptables off

2. Stop iptables using commands
	-sudo /etc/init.d/iptables stop

###Disable SELinux
1. navigate to the config file with root priviledges using
	-sudo vi /etc/selinux/config

2. Set the value of SELinux to disabled so the line should read:
	-SELINUX=disabled

3. Temoparily disable SELinux using the command
	-sudo setenforce 0

###Create saved image on Hortonworks

##Install Ambari Server

###Get Ambari server repository
1. install wget using
	-sudo yum install wget

2. Retrieve the repositories using:
	-sudo wget -nv http://public-repo-1.hortonworks.com/ambari/centos6/2.x/updates/2.0.1/ambari.repo -O /etc/yum.repos.d/ambari.repo

3. Run "yum repolist" command to ensure that atleast 4 packets were retreived (Updates-ambari-2.0.1,base, extras, updates)

4. Install the ambari server using
	-sudo yum install ambari-server

###Setup Ambari Server
1. Start the setup process using
	- sudo ambari-server setup

2. enter "y" when prompted

3. enter "n" when prompted

4. enter "1" and "y" when prompted in order to install the latest supported JDK

5. enter "n" when prompted to enter advanced database configuration

###Start the ambari server

1. Start the ambari server using
	-sudo ambari-server start

2. Make sure the ambari server is running using
	- sudo ambari-server status

##Configure Server and Deploying Agents

###Setup X11 forwarding
1. open /etc/ssh/sshd_config with root priveledges in a text editor

2. make sure X11Forwarding is set to yes
	- should read X11Forwarding=yes

3. Reload sshd
	-sudo /etc/init.d/sshd reload

4. Install xauth
	-sudo yum install xauth

5. Create new machine-id file using
	-sudo touch /var/lib/dbus/machine-id

6. run and copy the result
	-sudo dbus-uuidgen

7. Open /var/lib/dbus/machine-id with root privileges in a text editor and paste the uuid you just copied

5. Relog into the server with
	-ssh -X -A -i .pem cc@floatingIP

###Download google chrome
1. run command
	-sudo wget http://chrome.richardlloyd.org.uk/install_chrome.sh

2. run command to change permissions
	-sudo chmod u+x install_chrome.sh

3. execute the install_chrome.sh using
	-sudo ./install_chrome.sh

##Run Jobs