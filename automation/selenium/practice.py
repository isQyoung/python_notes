import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 隐藏浏览器测试提醒
options.add_argument('-ignore-certificate-errors')  # 忽略证书错误
# options.add_argument('-headless')  # 无头模式
options.add_argument('--user-data-dir=' + r'C:/Users/qyoung/AppData/Local/Google/Chrome/User Data/')
remote_url = 'http://127.0.0.1:9515'
options.add_argument(f'--remote-debugging-address={remote_url}')
driver = webdriver.Remote(command_executor=remote_url, options=options)
# 隐形等待时间3秒
driver.implicitly_wait(3)
driver.maximize_window()  # 全屏
# 打开地址
driver.get("https://www.eforest.finance/aelfinscription")
time.sleep(10)
# 点击登录选择插件
driver.find_element(By.XPATH, '//*[@id="portkey-ui-root"]/section/div/div[2]/button').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="portkey-ui-root"]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[2]/div[1]/div[1]').click()
# 输入密码解锁并确定
driver.find_element(By.ID, "unlock_password").send_keys("Gnayuiq0")
driver.find_element(By.XPATH, '//*[@id="unlock_password"]').send_keys("Gnayuiq0")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="unlock"]/div[2]/div/div/div/div/button').click()
time.sleep(60)
