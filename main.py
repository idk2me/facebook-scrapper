from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from Data import Data

url = 'https://developers.facebook.com/docs/plugins/page-plugin/'
driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
button = driver.find_element('css selector', '._42ft._4jy0._9xo6._4jy3._4jy1.selected._51sy')
button.click()
search = driver.find_element('css selector', '.inputtext._55r1._55r2.inputtext.wideinputtext')
search.clear()
search.send_keys('https://www.facebook.com/jessicaShywouh')
# For some reason, this won't work if you don't use By object and specify FullXPATH
button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[5]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/div/div[2]/div/div[3]/a")
sleep(2)
button.click()
sleep(10)
script_box = driver.find_elements('css selector', '.prettyprint._3t10.prettyprinted')
script = script_box[0].text
print(type(script))

data = Data(html, script)
data.get_nonce()
driver.quit()