# Reference: https://pythonspot.com/selenium-get-links/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class J4MGetLinks(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_links(self):
		driver = self.driver

		driver.get("http://www.jokes4miles.com")

		for a in driver.find_elements_by_xpath('.//a'):
			print(a.get_attribute('href'))

	def tearDown(self):
		time.sleep(5)
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()