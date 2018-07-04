## Reference: https://pythonspot.com/selenium-get-links/

from selenium import webdriver
import time
 
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()
 
driver.get('https://www.jokes4miles.com')
for a in driver.find_elements_by_xpath('.//a'):
    print(a.get_attribute('href'))

time.sleep(4)
## Closes one tab.
# driver.close()
## Closes entire browser.
driver.quit()