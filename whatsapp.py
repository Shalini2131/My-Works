from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='C:/Users/shalu kallepalli/chromeDriver/chromedriver.exe')

driver.get("https://web.whatsapp.com")

input("please scan QR code and press any key to continue:")

msg = driver.find_element_by_css_selector('span[title="Srivaccha"]')
msg.click()
testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
time.sleep(600)
for i in range(100):
    testinput.send_keys("Happy Birthday :)")
    testinput.send_keys(Keys.RETURN)
