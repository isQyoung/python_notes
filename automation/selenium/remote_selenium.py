import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 隐藏浏览器测试提醒
options.add_argument('-ignore-certificate-errors')  # 忽略证书错误
# options.add_argument('-headless')  # 无头模式
remote_url = 'http://127.0.0.1:9515'
options.add_argument(f'--remote-debugging-address={remote_url}')
driver = webdriver.Remote(command_executor=remote_url, options=options)
# 隐形等待时间3秒
driver.implicitly_wait(3)
driver.maximize_window()  # 全屏
driver.get("http://10.0.0.1/")
# driver.save_screenshot("1.png")
time.sleep(1)
driver.find_element(By.NAME, 'usernameIpt').send_keys("admin")
driver.find_element(By.NAME, 'password').send_keys("123456")
driver.find_element(By.ID, 'loginSubmit').click()
time.sleep(2)
driver.refresh()  # 刷新
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'layui-nav-more').click()
driver.find_element(By.XPATH, '//*[@id="layui-menu"]/ul/li[2]/dl/dd[1]/a/span').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="tableRight"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/span').click()
driver.find_element(By.XPATH, '//*[@id="tableRight"]/div[2]/div[2]/div/div[3]/form/div[1]/div/div[1]/div/div/i').click()
driver.find_element(By.XPATH,
                    '//*[@id="tableRight"]/div[2]/div[2]/div/div[3]/form/div[1]/div/div[1]/div/dl/dd[3]').click()
driver.find_element(By.XPATH, '//*[@id="tableRight"]/div[2]/div[2]/div/div[3]/form/div[1]/div/div[2]/div/div/i').click()
driver.find_element(By.XPATH,
                    '//*[@id="tableRight"]/div[2]/div[2]/div/div[3]/form/div[1]/div/div[2]/div/dl/dd[3]').click()
driver.find_element(By.NAME, 'setKey').send_keys("192.165.1")
driver.find_element(By.XPATH, '//*[@id="tableRight"]/div[2]/div[2]/div/div[3]/div/a[1]').click()
print(driver.title)
time.sleep(30)
driver.quit()
