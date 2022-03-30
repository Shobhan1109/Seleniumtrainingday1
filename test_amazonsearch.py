import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started.")
driver.maximize_window()
driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=58075519359&hvpone=&hvptwo=&hvadid=486462756371&hvpos=&hvnetw=g&hvrand=2897238854787280647&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9300762&hvtargid=kwd-64107830&hydadcr=14452_2154371&gclid=Cj0KCQjw_4-SBhCgARIsAAlegrUS799kAYPnb3WOBWl-hmW_uOcr_yj12drfckPFsCGC_dYw0OtdBfkaAgwAEALw_wcB")
time.sleep(1)
driver.find_element_by_id("twotabsearchtextbox").send_keys("samsung s20")
time.sleep(2)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(6)
driver.close()
print("Test case completed.")