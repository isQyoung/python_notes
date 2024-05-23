# 网页访问登录示例
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 隐藏浏览器测试提醒
options.add_argument('-ignore-certificate-errors')  # 忽略证书错误
# options.add_argument('-headless')  # 无头模式
# 远程selenium服务，使用服务端的谷歌浏览器
# driver = webdriver.Remote(command_executor="http://192.165.4.99:4444/wd/hub",options=options)
# 本地驱动，使用本地谷歌浏览器
service_path = Service('chromedriver.exe')
driver = webdriver.Chrome(options=options, service=service_path)
driver.implicitly_wait(3)  # 隐形等待时间3秒
driver.maximize_window()  # 全屏
driver.get('https://www.baidu.com/')
# driver.find_element(By.ID, "name").send_keys("admin")  # 输入用户名
# driver.find_element(By.ID, "password").send_keys("123456")  # 输入密码
# time.sleep(1)
# driver.find_element(By.ID, 'enter').click()   # 登陆
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]/div[1]/input').send_keys("admin")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]/div[2]/input').send_keys("123456")
# # #driver.find_element_by_css_selector("verticalTop").send_keys("admin")  # 输入用户名
# # #driver.find_element_by_css_selector("placeholderInput verticalTop").send_keys("sangfor@2021")  # 输入密码
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="loginSubmit"]').click()  # 登录到首页
# time.sleep(1)
# driver.refresh()  # 刷新
# time.sleep(1)
# driver.find_element(By.XPATH,'/html/body/div[2]/div/a[2]').click()    # 点击终端管理
# time.sleep(1)
#
# driver.switch_to.frame("mainFrame")  # 跳转到iframe框架
# driver.find_element(By.ID,'filter').send_keys("192.165.1.99")  # 输入IP
print(driver.title)
time.sleep(30)
driver.quit()
