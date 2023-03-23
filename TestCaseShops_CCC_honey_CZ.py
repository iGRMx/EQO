from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
#--Chrome Browser
service_obj = Service("O:\QA\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.get("https://eqolabel.com/cs/news/8594006380249/")
driver.find_element(By.XPATH, "//a[normalize-space()='Decline']").click() #cookies

#getting prices from the 1. shop
EQO_CCC = driver.find_element(By.XPATH, "(//*[contains(text(), 'Kč')])[1]").text #price of CCC shop
shop1EQObutton = "https://eshop.cesky-cerny-cesnek.cz/cesky-cerny-cesnek-s-medem-370g/"
driver.find_element(By.XPATH, "(//a[@role='button'])[3]").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
CCC = driver.find_element(By.CSS_SELECTOR, ".price-final-holder").text
shop1button = driver.current_url
print(shop1button)
driver.close()
driver.switch_to.window(windowsOpened[0])
print(EQO_CCC)
print(CCC)

#getting prices from the 2. shop
EQO_Moravia = driver.find_element(By.XPATH, "(//*[contains(text(), 'Kč')])[2]").text #price of Moravia Garlic shop
shop2EQObutton = "https://www.moraviagarlic.cz/cerny-cesnek/c-cesky-cerny-cesnek-s-medem-370g/"
driver.find_element(By.XPATH, "(//a[@role='button'])[4]").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
Moravia = driver.find_element(By.CLASS_NAME, "price-final-holder").text
shop2button = driver.current_url
print(shop2button)
driver.close()
driver.switch_to.window(windowsOpened[0])
print(EQO_Moravia)
print(Moravia)



#checking
assert EQO_CCC == CCC
assert EQO_Moravia == Moravia

assert shop1EQObutton == shop1button
assert shop2EQObutton == shop2button
