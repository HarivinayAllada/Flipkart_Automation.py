# importing pytest module
import pytest

# importing webdriver from selenium module
from selenium import webdriver

# importing By from selenium module
from selenium.webdriver.common.by import By

# importing ActionChains from selenium module
from selenium.webdriver.common.action_chains import ActionChains

# Importing time
import time

# adding path of the chrome webdriver
# used to automate the browser
driver = webdriver.Chrome("C:\\Users\\vinay\\Downloads\\chromedriver_win32\\chromedriver.exe")
@pytest.fixture()
#to open the flipkart website on chrome browser
def test_chrome():
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    x = driver.title
    assert x == 'Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!'

# logging into the flipkart website
def test_login(test_chrome):
    driver.find_element(By.XPATH, '//input[@class="_2IX_2- VJZDxU"]').send_keys("7989230630")
    driver.find_element(By.XPATH, '//input[@class="_2IX_2- _3mctLh VJZDxU"]').send_keys("Pandugadu@45")
    driver.find_element(By.XPATH, '//button[@class="_2KpZ6l _2HKlqd _3AWRsL"]').click()
    time.sleep(5)

# to click on the account and moving into wishlist
def test_wishlist(test_chrome):
    actions = ActionChains(driver)
    hari = driver.find_element(By.XPATH, '//div[text()="Harivinay"]')
    actions.move_to_element(hari).perform()
    wish = driver.find_element(By.XPATH, '//div[text()="Wishlist"]')
    actions.move_to_element(wish).click().perform()
    time.sleep(5)

# adding an item to add to cart
def test_addToCart(test_chrome):
    driver.find_element(By.XPATH,'//div[@class="_3hscEA" and text()="OnePlus Nord Buds Bluetooth Headset"]').click()
    # opening another window
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.CLASS_NAME,"_36yFo0").send_keys("500072")
    driver.find_element(By.CLASS_NAME,"_2P_LDn").click()
    driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _2U9uOA _3v1-ww"]').click()
    print(driver.title)
    time.sleep(10)

# checking whether the item added to cart or not
def test_check(test_chrome):
    driver.back()
    driver.find_element(By.XPATH,'//a[@href="/viewcart?exploreMode=true&preference=FLIPKART"]').click()

# close the window
# quit from the browser
def test_close(test_chrome):
    driver.close()
    driver.quit()