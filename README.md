# Docker-Dashboard
Docker-Dashboard</br>
Note : </br>
Install following prerequsit to run this app
</br>
Install docker by using below url:
</br>
https://docs.docker.com/engine/installation/linux/ubuntulinux/</br>
$ pip install docker-py </br>
$ sudo pip install Flask</br>

To run Server : python user.py</br>
Login :</br>
Id : admin@gmail.com</br>
Pass: admin
</br>
download the zip:
</br>
https://github.com/ajinkyamhatre/Docker-Dashboard/archive/master.zip
</br></br>
 

cd /Docker-Dashboard-master
</br>
mkdir templates </br>
copy login.html & admin.html -> templates</br></br>

 

if you are using this dashboard remotely change the ip in Docker-Dashboard/blob/master/user.py in below line

 
</br>
app.run(‘<ip>’,8080,debug=True)

 </br>

and use url http://[ip]:8080/login

 

 
</br>
 

otherwise if u are running this code locally don’t change Docker-Dashboard/blob/master/user.py file

 
</br>
and access url is http://localhost:8080/login

 

 
