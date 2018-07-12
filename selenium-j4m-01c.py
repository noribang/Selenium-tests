## Reference: http://selenium-python.readthedocs.io/getting-started.html ##

# import time 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# checkContent = input("Enter content to test: ")
# print(checkContent)

# List that will contain celebrity names as strings to test for content.
contentList = []
lengthContentList = 4

# Get user input of celebrity names to check content and append it to list.
while len(contentList) < lengthContentList:
    checkContent = raw_input("Enter content to test: ")
    print(checkContent)
    contentList.append(checkContent)

# Create of instance of webdriver for Firefox browser.
#a. This will open Firefox browser.
## driver = webdriver.Firefox()
#b. This will open Chrome browser.
driver = webdriver.Chrome()


# Loop through list to check for content.
for i in contentList:
    # Webdriver instance will navigate to URL that has been passed to get(). 
    driver.get("http://www.jokes4miles.com/jokescontent?category")
    # Check if string provided is in title element.
    assert "Jokes4Miles - Content" in driver.title
    # Find the element by id attribute.
    elem = driver.find_element_by_id("content-search")
    # Print element found to shell.
    print("elem is: " + str(elem))
	# Clear input.
    elem.clear()
    # Print list item to shell.
    print(i) 
	# Send string passed into method to element found.
    elem.send_keys(i)
	# Programmatically enter Return key by calling send_key().
    elem.send_keys(Keys.RETURN)
	
	# Check if string provided is NOT IN the html of the page.
    assert "No results found." not in driver.page_source
    # Wait 3 seconds.
    sleep(3)

# Wait 5 seconds.
sleep(5)
# close() closes one tab.
## driver.close()
# quit() closes entire browser.
driver.quit()