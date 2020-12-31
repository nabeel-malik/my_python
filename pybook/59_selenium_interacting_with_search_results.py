"""
Now let's go ahead and interact with search results on www.techwithtim.net
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys     # gives access to keys, like Enter, Esc etc.

# following imports added for explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Appl/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# open a webpage
driver.get("https://techwithtim.net")

# Now let's try to search for 'test' using the search bar
# When looking for an element try to search for id, name or class, in that order.
search = driver.find_element_by_name("s")       # assign search bar element name to variable
search.clear()                                  # clear any pre-existing text from search bar
search.send_keys("test")                        # type 'test' in search bar
search.send_keys(Keys.RETURN)                   # hit 'Enter'

# add explicit wait for webpage elements to load
# https://selenium-python.readthedocs.io/waits.html#explicit-waits
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    # find all articles inside main
    articles = main.find_elements_by_tag_name("article")                        # note usage of .find_elements_

    # print summary for each article
    for article in articles:
        summary = article.find_element_by_class_name("entry-summary")           # note usage of .find_element_
        print(summary.text)

except:
    driver.quit()

finally:
    driver.quit()

"""
In the above example, note that '.find_element' returns single item, whereas '.find_elements_' returns list.
"""



