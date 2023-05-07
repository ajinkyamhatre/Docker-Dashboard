from docker import Client

connection = Client(base_url='unix://var/run/docker.sock')


def containers_list(running):
    if running:
        return connection.containers()
    else:
        lst = connection.containers(all=True)


def images_list():
    return connection.images()


def docker_info():
    return connection.info()


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
    connection.remove_container(mycont)


def start(mycont):
    connection.start(mycont)


def stop(mycont):
    connection.stop(mycont)


def create_container(image, command, name):
    connection.create_container(image=image, command=command, name=name)


def test():
    return connection.networks()


def network():
    return connection.networks()
