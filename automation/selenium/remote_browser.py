from selenium import webdriver


def remote_chrome(remote_dir):
    # 隐藏浏览器测试提醒 忽略证书错误 使用远程url和路径
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument('-ignore-certificate-errors')
    print(remote_dir)
    #options.add_argument(f'--user-data-dir={remote_dir}')
    return options


if __name__ == "__main__":
    # 浏览器远程url和路径
    #remote_url = 'http://127.0.0.1:9515'
    remote_url = 'http://192.165.4.99:9515'
    remote_dir = r'C:/Users/qyoung/AppData/Local/Google/Chrome/User Data/'
    options = remote_chrome(remote_dir)
    driver = webdriver.Remote(command_executor=remote_url, options=options)

    driver.get("chrome://version/")
    import time

    time.sleep(10)
    driver.quit()
