import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
username=input("Enter use name")
password=input("Enter the pass")
print("test case started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys(username)
time.sleep(1)
driver.find_element_by_name("pass").send_keys(password)
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(3)
driver.close()
print("test case succesfully completed")