"""
ActionChains are a way to automate low level interactions such as mouse movements, mouse button actions,
key press, and context menu interactions.
This is useful for doing more complex actions like hover over and drag and drop.

Remember: QUEUE and PERFORM!
When you call methods for actions on the ActionChains object, the actions are stored in a queue in the
ActionChains object. When you call perform(), the events are fired in the order they are queued up.

Let's automate the playing of the Cookie Clicker game using Selenium ActionChains.
Play to game to understand what the program is trying to achieve.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:/Appl/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker")

# implicitly wait for website to load
driver.implicitly_wait(5)

# define elements
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

# create list of items to buy, trying to buy the more advanced items first.
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):                                   # maximum 5000 clicks
    actions.perform()                                   # click cookie
    count = int(cookie_count.text.split(" ")[0])        # get cookie count from element
    for item in items:                                  # loop through items to buy
        price = int(item.text)                          # find item price
        if price <= count:                              # can we buy item?
            buy_actions = ActionChains(driver)          # set ActionChain to buy item
            buy_actions.move_to_element(item)
            buy_actions.click()
            buy_actions.perform()