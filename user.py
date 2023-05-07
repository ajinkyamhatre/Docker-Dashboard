from mydocker import docker_info, containers_list, images_list, memory, remove, start, stop, create_container, test, network
import subprocess
from flask import *

app = Flask(__name__)
app.secret_key = 'my key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    session['logged_in'] = False
    if request.method == 'POST':
        if request.form['email'] == 'admin@gmail.com' and request.form['password'] == 'admin':
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return "<h1>wrong password</h1>"
    else:
        return render_template('login.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    action_list = []
    all_containers_list = containers_list(running=False)
    if session['logged_in']:
        myimg = ''
        if request.method == 'POST' or 'GET':
            for container in containers_list(running=False):
                if request.form.getlist(container['Id'][0:12]):
                    action_list.append(container['Id'][0:12])
            if request.form.getlist('remove'):
                for container in action_list:
                    remove(container)
            if request.form.getlist('start'):
                for container in action_list:
                    start(container)
            if request.form.getlist('stop'):
                for container in action_list:
                    stop(container)
            for image in images_list():
                if request.form.getlist(image['Id'][7:19]):
                    image_name = (image['Id'][7:19])
                    create_container(image=image_name, command=request.form['command'], name=request.form['name'])
        return render_template('admin.html', mymemory=memory(), cont=docker_info(), lst=all_containers_list)
    else:
        return redirect(url_for('myrequest'))


@app.route('/create', methods=['GET', 'POST'])
def image_admin():
    lst = containers_list(running=False)
    img_lst = images_list()
    action_list = []
    if session['logged_in']:
        myimg = ''
        if request.method == 'POST':
            for i in img_lst:
                if request.form.getlist(i['Id'][7:19]):
                    myimg = (i['Id'][7:19])
            create_container(image=myimg, command=request.form['command'], name=str(request.form['name']))

        return render_template('admin.html', mymemory=memory(), cont=docker_info(), img=images_list())
    else:
        return redirect(url_for('myrequest'))


@app.route('/network', methods=['GET', 'POST'])
def network_admin():
    lst = containers_list(running=False)
    img_lst = images_list()
    action_list = []
    if session['logged_in']:
        myimg = ''
        if request.method == 'POST':
            for i in img_lst:
                if request.form.getlist(i['Id'][7:19]):
                    myimg = (i['Id'][7:19])
            create_container(image=myimg, command=request.form['command'], name=str(request.form['name']))

        return render_template('admin.html', mymemory=memory(), cont=docker_info(), net=network())
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/')
def first():
    session['logged_in'] = False
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True)
