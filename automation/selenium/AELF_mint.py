import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 解锁密码 浏览器远程url和路径
unlock_pass = "123456"
remote_url = 'http://127.0.0.1:9515'
remote_dir = r'C:/Users/qyoung/AppData/Local/Google/Chrome/User Data/'
mint_url = "https://www.eforest.finance/aelfinscription/inscription-detail?tick=NEWBEE"
mint = "100"

# 隐藏浏览器测试提醒 忽略证书错误 使用远程url和路径
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_argument('-ignore-certificate-errors')
options.add_argument(f'--remote-debugging-address={remote_url}')
options.add_argument(f'--user-data-dir={remote_dir}')
# 启动远程浏览器
driver = webdriver.Remote(command_executor=remote_url, options=options)
# 隐形等待时间3秒
driver.implicitly_wait(3)
# 打开地址
time.sleep(2)
driver.get(mint_url)
time.sleep(10)

# 获取所有窗口句柄
window_handles = driver.window_handles
# 记录当前窗口句柄
current_window_handle = driver.current_window_handle
# 切换到非Selenium WebDriver打开的窗口句柄，假设目标窗口句柄是最新打开的窗口句柄
target_window_handle = window_handles[-1]
driver.switch_to.window(target_window_handle)
# 输入密码解锁并确定
driver.find_element(By.ID, "unlock_password").send_keys(unlock_pass)
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="unlock"]/div[2]/div/div/div/div/button').click()
time.sleep(3)
# 切回原来的页面
driver.switch_to.window(current_window_handle)

count = 0
while True:
    time.sleep(5)
    # mint数量16 点击mint
    driver.find_element(By.XPATH, '//*[@id="marketplace-content"]/div[1]/div/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH,
                        "/html/body/div[3]/div[2]/div/div[2]/div[2]/form/div[2]/div/div[2]/div/div/div/input").send_keys(
        mint)
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[3]/button').click()
    time.sleep(10)
    # 获取所有窗口句柄
    window_handles = driver.window_handles
    # 记录当前窗口句柄
    current_window_handle = driver.current_window_handle
    target_window_handle = window_handles[-1]
    driver.switch_to.window(target_window_handle)
    # 点击sign
    driver.find_element(By.XPATH, '//*[@id="portkey-ui-root"]/div[1]/div[4]/button[2]/span').click()
    # 切回
    driver.switch_to.window(current_window_handle)
    # 刷新页面
    time.sleep(30)
    driver.refresh()
    count += 1
    print(str(count))
