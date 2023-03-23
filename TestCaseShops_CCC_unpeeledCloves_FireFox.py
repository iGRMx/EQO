from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#--Firefox
driver = webdriver.Firefox()
driver.get("https://eqolabel.com/news/cesky-cerny-cesnek-unpeeled-cloves-60g/")
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//a[normalize-space()='Decline']").click() #cookies
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#getting prices from the 1. shop
EQO_CCC = driver.find_element(By.XPATH, "(//*[contains(text(), 'Kč')])[1]").text #price of CCC shop
shop1EQObutton = "https://eshop.cesky-cerny-cesnek.cz/cerny-cesnek-z-ceska-neloupany-v-sacku-60g/"
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

#check the button of the 2. shop
shop2EQObutton = "https://www.mall.cz/lekarna/cesky-cerny-cesnek-neloupane-strouzky-cerneho-100039318727"
driver.find_element(By.XPATH, "(//a[@role='button'])[4]").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.CSS_SELECTOR, "div[class='tps the-price-section'] span[class='price-section-redesign__price'] span").text)
shop2button = driver.current_url
print(shop2button)
driver.close()
driver.switch_to.window(windowsOpened[0])

#getting prices from the 3. shop
EQO_Moravia = driver.find_element(By.XPATH, "(//*[contains(text(), 'Kč')])[2]").text #price of Moravia Garlic shop
shop3EQObutton = "https://www.moraviagarlic.cz/cerny-cesnek/c-cesky-cerny-cesnek--neloupane-strouzky--60g/"
driver.find_element(By.XPATH, "(//a[@role='button'])[5]").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
Moravia = driver.find_element(By.CLASS_NAME, "price-final-holder").text
shop3button = driver.current_url
print(shop3button)
driver.close()
driver.switch_to.window(windowsOpened[0])
print(EQO_Moravia)
print(Moravia)

#getting prices from the 4. shop
EQO_Koreni = driver.find_element(By.XPATH, "(//*[contains(text(), 'Kč')])[3]").text #price of LevneKoreni Shop
shop4EQObutton = "https://www.levnekoreni.cz/koreni/jednodruhove-koreni/cesky-cerny-cesnek/"
driver.find_element(By.XPATH, "(//a[@role='button'])[6]").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
Koreni = driver.find_element(By.XPATH, "//div[@class='addBasket'][1]//strong[contains(text(),'Kč')]").text
shop4button = driver.current_url
print(shop4button)
driver.close()
driver.switch_to.window(windowsOpened[0])
print(EQO_Koreni)
print(Koreni)


#checking
assert EQO_CCC == CCC
assert EQO_Moravia == Moravia
assert EQO_Koreni == Koreni
assert shop1EQObutton == shop1button
assert shop2EQObutton == shop2button
assert shop3EQObutton == shop3button
assert shop4EQObutton == shop4button