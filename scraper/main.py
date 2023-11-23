from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from Data import Data

class Nonce:
    def __init__(self, url: str, page_url: str):
        self.url = url
        self.page_url = page_url
    
    def run(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        button = driver.find_element('css selector', '._42ft._4jy0._9xo6._4jy3._4jy1.selected._51sy')
        button.click()
        search = driver.find_element('css selector', '.inputtext._55r1._55r2.inputtext.wideinputtext')
        search.clear()
        search.send_keys(self.page_url)
        # For some reason, this won't work if you don't use By object and specify FullXPATH
        button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[5]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/div/div[2]/div/div[3]/a")
        sleep(1)
        button.click()
        sleep(1)
        script = driver.find_elements('css selector', '.prettyprint._3t10.prettyprinted')[0].text
        driver.quit()
        data = Data(script)
        return data.get_nonce()