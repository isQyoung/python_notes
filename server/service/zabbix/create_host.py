import requests
import json


def create_data(data):
    common_data = {"jsonrpc": "2.0", "method": data[0], "params": data[1], "id": 1}
    return common_data


def request_data(url, data, headers):
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()


def create_host(url, api_token, host, host_group, template_host):
    # 验证头
    headers = {'Content-Type': 'application/json-rpc', 'Authorization': f'Bearer {api_token}'}
    # 获取组id
    data = ['hostgroup.get', {"output": "extend", "filter": {"name": [host_group]}}]
    data = create_data(data)
    response = request_data(url, data, headers)
    groupid = response['result'][0]['groupid']
    # 获取模板id
    data = ['template.get', {"output": "extend", "filter": {"host": [template_host]}}]
    data = create_data(data)
    response = request_data(url, data, headers)
    templateid = response['result'][0]['templateid']
    # 创建主机
    data = ['host.create', {'host': host, 'interfaces': [
        {'type': 1, 'main': 1, 'useip': 1, 'ip': '0.0.0.0', 'dns': '', 'port': '10050'}],
                            'groups': [{'groupid': groupid}], 'templates': [{'templateid': templateid}],
                            'inventory_mode': 0}]
    data = create_data(data)
    response = request_data(url, data, headers)
    return response


if __name__ == '__main__':
    host = 'test1234567890'
    url = 'https://zabbix.xxx.com/api_jsonrpc.php'
    api_token = 'abcdefghijklmn'
    host_group = '新系统'
    template_host = 'Linux-Server-General-All'
    result = create_host(url, api_token, host, host_group, template_host)
    if result['error']:
        print(result['error']['data'])
    else:
        print('创建成功')
