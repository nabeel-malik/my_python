# https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys     # gives access to keys, like Enter, Esc etc.
import time

PATH = "C:/Appl/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# open a webpage
driver.get("https://techwithtim.net")

# close current tab
# driver.close()

# print webpage title
print(driver.title)

# close entire browser
# driver.quit()

# Now let's try to search for 'test' using the search bar
# When looking for an element try to search for id, name or class, in that order.
search = driver.find_element_by_name("s")       # assign search bar element name to variable
search.clear()                                  # clear any pre-existing text from search bar
search.send_keys("test")                        # type 'test' in search bar
search.send_keys(Keys.RETURN)                   # hit 'Enter'

# you could print page source code for the search results page
# print(driver.page_source)

# wait for 10 seconds and quit browser
time.sleep(10)
driver.quit()





