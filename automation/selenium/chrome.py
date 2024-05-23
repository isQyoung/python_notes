import time
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 隐藏浏览器测试提醒
options.add_argument('-ignore-certificate-errors')  # 忽略证书错误
# 指定本地驱动，使用本地谷歌浏览器
#from selenium.webdriver.chrome.service import Service
#service_path = Service('chromedriver.exe')
#driver = webdriver.Chrome(options=options, service=service_path)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)   # 隐形等待时间3秒
driver.maximize_window()   # 全屏
driver.get("https://www.baidu.com")

time.sleep(5)
driver.execute_script("window.open('about:blank','_blank');")
time.sleep(1)
# 获取当前窗口句柄列表
window_handles = driver.window_handles

# 切换到新创建的页面
driver.switch_to.window(window_handles[-1])
driver.get("https://www.qq.com")

time.sleep(5)
# 切回来
driver.switch_to.window(window_handles[0])
time.sleep(5)
# 切回去
driver.switch_to.window(window_handles[-1])
time.sleep(5)
driver.quit()
