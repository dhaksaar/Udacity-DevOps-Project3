# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from datetime import datetime


# Start the browser and login with standard_user
def login (user, password):
    print (datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'\tStarting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'\tBrowser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    inventory_label = driver.find_element_by_css_selector("div[class='inventory_item_label']").text
    print(inventory_label)
    assert "Sauce Labs Backpack" in inventory_label
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'\tLoggged in  with username {:s} and password {:s} successfully'.format(user, password))
    return driver

def addToCart(driver):
    inventories = driver.find_elements_by_class_name('inventory_item_name')
    itemCount = len (inventories)
    for itemIndex in range(itemCount):
        item= driver.find_elements_by_class_name('inventory_item_name')[itemIndex]
        item.click()
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'\tNavigated to url:'+driver.current_url)
        btnAdd = driver.find_element_by_class_name('btn_inventory')
        btnAdd.click()
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'\tAdded inventory {:s} to cart'.format(driver.find_element_by_class_name("inventory_details_name").text))
        backBtn = driver.find_element_by_id('back-to-products')
        backBtn.click()
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'\tNavigated to url:'+driver.current_url)
     

def removeFromCart(driver):
    inventories = driver.find_elements_by_class_name('inventory_item_name')
    itemCount = len (inventories)
    for itemIndex in range(itemCount):
        item= driver.find_elements_by_class_name('inventory_item_name')[itemIndex]
        item.click()
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'\tNavigated to url:'+driver.current_url)
        btnAdd = driver.find_element_by_class_name('btn_inventory')
        btnAdd.click()
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tRemove inventory {:s} from cart'.format(driver.find_element_by_class_name("inventory_details_name").text))
        backBtn = driver.find_element_by_id('back-to-products')
        backBtn.click()
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'\tNavigated to url:'+driver.current_url)
     

driver = login('standard_user', 'secret_sauce')
addToCart(driver)
removeFromCart(driver)
driver.quit()
