#ACX cluster Spark setup for data science course documentation

##Launching instances
1. Launch 1 master Ubuntu 14.04 large instance on nova

2. Associate floating IP with the master node

3. Launch 4 slave Ubuntu 14.04 large instances on nova

##Master instance setup
1. ssh into the master node
```
ssh -i neeraj-acx.pem ubuntu@$FLOATING_IP
```

2. Update the Ubuntu image
```
sudo apt-get update
```

3. Download Java (JDK)
```
sudo apt-get install default-jdk
```

4. 