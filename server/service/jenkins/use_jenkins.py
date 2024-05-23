import jenkins

server = jenkins.Jenkins('http://192.168.66.99:8080', username='admin', password='123456')
# 获取用户名和系统版本
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
# 获取所有job
jobs = server.get_jobs()
print(jobs)
# 获取指定view的job
jobs = server.get_jobs(view_name='all')
print(jobs)
# 构建job 获取构建号 构建信息
server.build_job('test-job')
last_build_number = server.get_job_info('test-job')['lastCompletedBuild']['number']
build_info = server.get_build_info('test-job', last_build_number)
print(build_info)
