from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.suning.com")
# driver.find_element(By.XPATH, "//*[@id='searchKeywords']").send_keys("rog5")
# driver.find_element(By.XPATH, "//*[@id='searchSubmit']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='0000000000-11359636513']/div/div/div[2]/div[2]/a").click()
# time.sleep(3)
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element(By.XPATH, "//*[@id='addCart']").click()
# time.sleep(2)
# driver.quit()

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.jd.com')
# driver.find_element(By.XPATH, "//*[@id='key']").send_keys("rog5")
# driver.find_element(By.XPATH, "//*[@aria-label='搜索' and @clstag='h|keycount|head|search_a']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[1]/div[1]/div[1]/div[3]/ul/li[1]/div[1]/div[3]/a').click()
# time.sleep(3)
# handles = driver.window_handles
# for handle in handles:
#     if handle != driver.current_window_handle:
#         driver.close()
#         driver.switch_to.window(handle)
# driver.find_element(By.XPATH, "//*[@id='InitCartUrl']").click()
# time.sleep(2)

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")
driver.find_element(By.XPATH, "//*[@x-webkit-grammar='builtin:translate']").send_keys("永劫无间")
driver.find_element(By.XPATH, "//*[@class='nav-search-btn-text']").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/div/div[1]/a").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[2])
driver.find_element(By.XPATH, "//*[@class='van-icon-videodetails_like']").click()
time.sleep(2)
driver.quit()
