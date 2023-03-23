from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
#--Chrome Browser
service_obj = Service("O:\QA\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.get("https://eqolabel.com/news/cesky-cerny-cesnek-unpeeled-cloves-60g/")
driver.find_element(By.XPATH, "//a[normalize-space()='Decline']").click() #cookies

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

#go to CZ language
driver.find_element(By.CSS_SELECTOR, "#menu-item-4077").click()
driver.find_element(By.CSS_SELECTOR, "#menu-item-4077-cs").click()

#getting prices from the 1. shop
EQO_CCC_CZ = driver.find_element(By.XPATH, "(//*[contains(text(), 'Kč')])[1]").text #price of CCC shop
shop1EQObutton_CZ = "https://eshop.cesky-cerny-cesnek.cz/cerny-cesnek-z-ceska-neloupany-v-sacku-60g/"
driver.find_element(By.XPATH, "(//a[@role='button'])[3]").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
CCC_CZ = driver.find_element(By.CSS_SELECTOR, ".price-final-holder").text
shop1button_CZ = driver.current_url
print(shop1button_CZ)
driver.close()
driver.switch_to.window(windowsOpened[0])
print(EQO_CCC_CZ)
print(CCC_CZ)

#check the button of the 2. shop
shop2EQObutton_CZ = "https://www.mall.cz/lekarna/cesky-cerny-cesnek-neloupane-strouzky-cerneho-100039318727"
driver.find_element(By.XPATH, "(//a[@role='button'])[4]").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.CSS_SELECTOR, "div[class='tps the-price-section'] span[class='price-section-redesign__price'] span").text)
shop2button_CZ = driver.current_url
print(shop2button_CZ)
driver.close()
driver.switch_to.window(windowsOpened[0])

#getting prices from the 3. shop
EQO_Moravia_CZ = driver.find_element(By.XPATH, "(//*[contains(text(), 'Kč')])[2]").text #price of Moravia Garlic shop
shop3EQObutton_CZ = "https://www.moraviagarlic.cz/cerny-cesnek/c-cesky-cerny-cesnek--neloupane-strouzky--60g/"
driver.find_element(By.XPATH, "(//a[@role='button'])[5]").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
Moravia_CZ = driver.find_element(By.CLASS_NAME, "price-final-holder").text
shop3button_CZ = driver.current_url
print(shop3button_CZ)
driver.close()
driver.switch_to.window(windowsOpened[0])
print(EQO_Moravia_CZ)
print(Moravia_CZ)

#getting prices from the 4. shop
EQO_Koreni_CZ = driver.find_element(By.XPATH, "(//*[contains(text(), 'Kč')])[3]").text #price of LevneKoreni Shop
shop4EQObutton_CZ = "https://www.levnekoreni.cz/koreni/jednodruhove-koreni/cesky-cerny-cesnek/"
driver.find_element(By.XPATH, "(//a[@role='button'])[6]").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
Koreni_CZ = driver.find_element(By.XPATH, "//div[@class='addBasket'][1]//strong[contains(text(),'Kč')]").text
shop4button_CZ = driver.current_url
print(shop4button_CZ)
driver.close()
driver.switch_to.window(windowsOpened[0])
print(EQO_Koreni_CZ)
print(Koreni_CZ)


#checking_CZ
assert EQO_CCC_CZ == CCC_CZ
assert EQO_Moravia_CZ == Moravia_CZ
assert EQO_Koreni_CZ == Koreni_CZ
assert shop1EQObutton_CZ == shop1button_CZ
assert shop2EQObutton_CZ == shop2button_CZ
assert shop3EQObutton_CZ == shop3button_CZ
assert shop4EQObutton_CZ == shop4button_CZ


