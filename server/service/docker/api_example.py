import os
import docker

# 连接
# http方式
# client = docker.DockerClient(base_url='http://192.165.1.108:2375')
# https方式一
os.environ['DOCKER_HOST'] = 'tcp://dapi.q.cn:2376'
os.environ['DOCKER_TLS_VERIFY'] = 'True'
os.environ['DOCKER_CERT_PATH'] = '.'
client = docker.from_env()
# https方式二
# tls_config = docker.tls.TLSConfig(ca_cert='ca.pem', client_cert=('cert.pem', 'key.pem'), verify=True)
# client = docker.DockerClient(base_url='tcp://dapi.q.cn:2376', tls=tls_config)
# print(client.version())
# print(client.info())

# 初始化swarm
# swarm_str = client.swarm.init()
# print(swarm_str)

# 配置config
config_dict = {'name': 'test_config', 'data': b'Hello World', 'templating': {'name': 'golang'}}
config_id = client.configs.create(**config_dict)
print(config_id)
config_object = client.configs.get('test_config')
config_object.remove()

# 容器container
container_dict = {'name': 'test', 'image': 'alpine', 'command': 'echo hello world', 'detach': True}
container_id = client.containers.run(**container_dict)
print(container_id)
containers_object = client.containers.get('test')
containers_rm = {'force': True}
containers_object.remove(**containers_rm)

# 镜像image
# image = client.images.pull('busybox')
# print(image)
# client.images.remove(image='busybox:latest')

# 网络network
network = client.networks.create("test_network", driver="overlay")
print(network)
network = client.networks.get('test_network')
network.remove()

# 节点node
node = client.nodes.list()
print(node)

# 秘密secrets
secrets_dict = {'name': 'test_secrets', 'data': b'Hello secrets'}
secrets = client.secrets.create(**secrets_dict)
print(secrets)
secrets = client.secrets.get('test_secrets')
secrets.remove()

# 服务service
service_dict = {'name': 'test', 'image': 'alpine', 'command': 'sleep 100000'}
service = client.services.create(**service_dict)
print(service)
service = client.services.get('test')
service.remove()

# 卷volume
volume_dict = {'name': 'test_volume', 'driver': 'local', 'labels': {"env": "test"}}
volume = client.volumes.create(**volume_dict)
print(volume)
volume = client.volumes.get('test_volume')
volume.remove()
