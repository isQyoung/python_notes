import requests

def get_ip():
    url='https://api.ipify.org/'
    r = requests.get(url)
    print(f'当前公网ip为: {r.text}')

def ip_detail():
    url = 'http://ip-api.com/json/?fields=61439&lang=zh-CN'
    r = requests.get(url)
    data = r.json()
    #print(data)
    detail = f'''
    ip: {data["query"]}
    归属地: {data["country"]}{data["regionName"]}
    代号: {data["countryCode"]} {data["region"]}
    时区: {data["timezone"]}
    '''
    print(detail)


if __name__ == '__main__':
    #get_ip()
    ip_detail()
