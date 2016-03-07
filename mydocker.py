from docker import Client
cli = Client(base_url='unix://var/run/docker.sock')
def containers_list(running):
	if running:
		lst=cli.containers()
		return lst
	else:
		lst=cli.containers(all=True)
		return lst
def images_list():
	return cli.images()
def myadd():
	return cli.info()
def memory():
    """
    Get node total memory and memory usage
    """
    with open('/proc/meminfo', 'r') as mem:
        ret = {}
        tmp = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) == 'MemTotal:':
                ret['total'] = int(sline[1])
            elif str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                tmp += int(sline[1])
        ret['free'] = tmp
        ret['used'] = int(ret['total']) - int(ret['free'])
    return ret
def remove(mycont):
	cli.remove_container(mycont)
def start(mycont):
	cli.start(mycont)
def stop(mycont):
	cli.stop(mycont)
def create_container(image,command,name):
	cli.create_container(image=image,command=command,name=name)
def test():
	return cli.networks()
def network():
	return cli.networks()

