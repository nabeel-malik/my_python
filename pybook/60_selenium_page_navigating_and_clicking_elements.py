"""
Now let's create a script to go to www.techwithtim.net, and navigate to:
1. Python Programming (in the TUTORIALS & GUIDES section)
2. Beginner Python Tutorials
3. Click "Get Started"
4. Go back all the way to homepage (3 backs)
5. Go forward all the way to the page after clicking "Get Started" (3 forwards)
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

try:
    # click on 'Python Programming' link (using EXPLICIT WAIT)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Python Programming"))
    )
    # click the element
    element.click()

    # click on 'Beginner Python Tutorials' link (using EXPLICIT WAIT)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    # click on 'Get Started' link (using EXPLICIT WAIT)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

except:
    driver.quit()

# go back all the way to homepage (3 backs)
driver.back()
driver.back()
driver.back()

# go forward all the way to the page after clicking "Get Started" (3 forwards)
driver.forward()
driver.forward()
driver.forward()

# wait for 10 seconds and quit browser
time.sleep(10)
driver.quit()




