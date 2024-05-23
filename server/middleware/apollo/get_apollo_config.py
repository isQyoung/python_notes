import time
import hashlib
import hmac
import base64
import requests


class GetConfig:
    def __init__(self, url, **kwargs):
        """初始化获取appid cluster application secret"""
        self.url = url
        self.appid = kwargs.get('appid', 'unknown')
        self.cluster = kwargs.get('cluster', 'default')
        self.application = kwargs.get('application', 'application')
        self.secret = kwargs.get('secret', '')

    def get_sign_string(self, string_to_sign):
        """获取验证字符串"""
        encoding = 'utf-8'
        try:
            key = bytes(self.secret, encoding)
            message = bytes(string_to_sign, encoding)
            signature = hmac.new(key, message, hashlib.sha1).digest()
            return base64.b64encode(signature).decode(encoding)
        except Exception as e:
            raise ValueError(str(e))

    def get_header(self, auth, timestamp):
        """获取请求所需header参数"""
        return {"Authorization": f"Apollo {self.appid}:{auth}", "Timestamp": str(timestamp)}

    def get_config(self):
        """获取指定的所有配置"""
        timestamp = int(time.time() * 1000)
        url_path = f'/configs/{self.appid}/{self.cluster}/{self.application}'
        string_to_sign = str(timestamp) + "\n" + url_path
        sign_string = self.get_sign_string(string_to_sign)
        all_url = self.url + url_path
        headers = self.get_header(sign_string, timestamp)
        response = requests.get(all_url, headers=headers)
        return response.json()["configurations"]


if __name__ == '__main__':
    """示例"""
    config = GetConfig('http://192.168.66.99:8080', appid="SampleApp", cluster="default", application="application",
                       secret="fec41b6bf269436991c08e26bb939d1a")
    print(config.get_config())