from mydocker import myadd ,containers_list ,images_list,memory,remove,start,stop,create_container,test,network

import subprocess
from flask import *

app=Flask(__name__)
app.secret_key = 'my key'

@app.route('/login', methods=['GET','POST'])
def myrequest():
	session['logged_in']=False
	if request.method == 'POST':
		if request.form['email']=='admin@gmail.com' and request.form['password']=='admin':
			session['logged_in']=True
			return redirect(url_for('admin'))
		
		else:
			return "<h1>wrong password</h1>"
	else:
		return render_template('login.html')
@app.route('/admin',methods=['GET', 'POST'])
def admin():
	lst=containers_list(running=False)
	img_lst=images_list()
	action_list=[]
	
	if session['logged_in']:
		myimg=''
		if request.method == 'POST' or 'GET':
			for c in lst:
				if request.form.getlist(c['Id'][0:12]):
					action_list.append(c['Id'][0:12])
			if request.form.getlist('remove'):
				for ch in action_list:
					remove(ch)
			if request.form.getlist('start'):
				for ch in action_list:
					start(ch)
			if request.form.getlist('stop'):
				for ch in action_list:
					stop(ch)
			for i in img_lst:
				if request.form.getlist(i['Id'][7:19]):
					myimg=(i['Id'][7:19])
			   		create_container(image=myimg,command=request.form['command'],name=request.form['name'])
		return render_template('admin.html',mymemory=memory(),cont=myadd(),lst=lst)
	else:
		return redirect(url_for('myrequest'))
@app.route('/create',methods=['GET', 'POST'])
def image_admin():
	lst=containers_list(running=False)
	img_lst=images_list()
	action_list=[]
	if session['logged_in']:
		myimg=''
		if request.method == 'POST':
			for i in img_lst:
				if request.form.getlist(i['Id'][7:19]):
					myimg=(i['Id'][7:19])
			create_container(image=myimg,command=request.form['command'],name=str(request.form['name']))
			
		return render_template('admin.html',mymemory=memory(),cont=myadd(),img=images_list())
	else:
		return redirect(url_for('myrequest'))

@app.route('/network',methods=['GET', 'POST'])
def network_admin():
	lst=containers_list(running=False)
	img_lst=images_list()
	action_list=[]
	if session['logged_in']:
		myimg=''
		if request.method == 'POST':
			for i in img_lst:
				if request.form.getlist(i['Id'][7:19]):
					myimg=(i['Id'][7:19])
			create_container(image=myimg,command=request.form['command'],name=str(request.form['name']))
			
		return render_template('admin.html',mymemory=memory(),cont=myadd(),net=network())
	else:
		return redirect(url_for('myrequest'))
@app.route('/logout')
def logout():
	session['logged_in']=False
	return redirect(url_for('myrequest'))

@app.route('/test')
def mytest():
	f=''
	ans=test()
	for c in ans:
		f=f+str(c)+"-------------------------------------</br></br></br></br>"
	return f
		

if __name__=="__main__":
        app.run('localhost',8080,debug=True)

