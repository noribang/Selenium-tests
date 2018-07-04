## Reference: http://selenium-python.readthedocs.io/getting-started.html ##

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class J4MTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_search_in_python_org(self):
		driver = self.driver
		# driver.get("http://www.python.org")
		driver.get("http://www.jokes4miles.com/jokescontent?category")
		# self.assertIn("Python", driver.title)
		self.assertIn("Jokes4Miles - Content", driver.title)
		# elem = driver.find_element_by_name("q")
		elem = driver.find_element_by_id("content-search")
		elem.clear()
		# elem.send_keys("pycon")
		elem.send_keys("pat tomasulo")
		elem.send_keys(Keys.RETURN)
		# assert "No results found." not in driver.page_source
		assert "Sorry, there is no content with the specified parameters!" not in driver.page_source

	def tearDown(self):
		time.sleep(4)
		# self.driver.close()

if __name__ == "__main__":
	unittest.main()