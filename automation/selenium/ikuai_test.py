from remote_browser import remote_chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 浏览器远程url和路径
remote_url = 'http://192.168.66.99:10003'
remote_dir = r'C:/Users/qyoung/AppData/Local/Google/Chrome/User Data/'
options = remote_chrome(remote_dir)
driver = webdriver.Remote(command_executor=remote_url, options=options)
driver.get("http://192.168.123.1")
# 等待元素可见，最长等待时间为10秒
wait = WebDriverWait(driver, 60)
user_element = wait.until(EC.visibility_of_element_located((By.ID, "usernameIpt")))
pass_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/form/ul/li[3]/div/input')))
login_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div > div.login.clearfix > form > ul > li:nth-child(4) > button")))
user_element.send_keys("admin")
pass_element.send_keys("123456")
login_element.click()
netset_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#toolsLi3 > a')))
netset_element.click()
port1_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="scrollContent2"]/ul/li[10]/a')))
port1_element.click()
port2_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="scrollContent2"]/ul/li[10]/ul/li[1]/a')))
port2_element.click()
search_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fantasyMenu"]/div[4]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/input[1]')))
search_element.send_keys("10809")
searchenter_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fantasyMenu"]/div[4]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/input[2]')))
searchenter_element.click()
