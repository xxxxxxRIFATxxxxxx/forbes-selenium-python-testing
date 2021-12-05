from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Setup Driver
driver = webdriver.Chrome(executable_path="E:/Programming Hero/Projects/forbes-selenium-python-testing/drivers/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

# Test
# Search function
driver.get("https://www.forbes.com/")
SEARCH_BUTTON = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header > /header > nav > div.header__right > button")
SEARCH_BUTTON.click()
SEARCH_INPUT = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header >div.search-modal > form > input")
SEARCH_INPUT.send_keys("Bangladesh")
SEARCH_INPUT.send_keys(Keys.RETURN)

# Most relevent
driver.get("https://www.forbes.com/")
SEARCH_BUTTON = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header > /header > nav > div.header__right > button")
SEARCH_BUTTON.click()
SEARCH_INPUT = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header >div.search-modal > form > input")
SEARCH_INPUT.send_keys("Bangladesh")
SEARCH_INPUT.send_keys(Keys.RETURN)
MOST_RELEVENT = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--overflow-visible.main-content--universal-header > main > div.search-content-wrapper > div.search-content.main-content__left-col > div.search-sort > div.search-sort__button.search-sort__button-relevant.search-sort__button--selected")
MOST_RELEVENT.click()

# Most recent
driver.get("https://www.forbes.com/")
SEARCH_BUTTON = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header > /header > nav > div.header__right > button")
SEARCH_BUTTON.click()
SEARCH_INPUT = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header >div.search-modal > form > input")
SEARCH_INPUT.send_keys("Bangladesh")
SEARCH_INPUT.send_keys(Keys.RETURN)
MOST_RECENT = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--overflow-visible.main-content--universal-header > main > div.search-content-wrapper > div.search-content.main-content__left-col > div.search-sort > div.search-sort__button.search-sort__button-recent")
MOST_RECENT.click()

# Time bar
# All Time
driver.get("https://www.forbes.com/")
SEARCH_BUTTON = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header > /header > nav > div.header__right > button")
SEARCH_BUTTON.click()
SEARCH_INPUT = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header >div.search-modal > form > input")
SEARCH_INPUT.send_keys("Bangladesh")
SEARCH_INPUT.send_keys(Keys.RETURN)
ALL_TIME = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--overflow-visible.main-content--universal-header > main > div.search-content-wrapper > div.search-content.main-content__left-col > div.search-sort > div.search-sort__dropdown")
ALL_TIME.click()

# Past Year
driver.get("https://www.forbes.com/")
SEARCH_BUTTON = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header > /header > nav > div.header__right > button")
SEARCH_BUTTON.click()
SEARCH_INPUT = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header >div.search-modal > form > input")
SEARCH_INPUT.send_keys("Bangladesh")
SEARCH_INPUT.send_keys(Keys.RETURN)
PAST_YEAR = (By.CSS_SELECTOR, "body > div.main-content.main-content--overflow-visible.main-content--universal-header > main > div.search-content-wrapper > div.search-content.main-content__left-col > div.search-sort > div.search-sort__dropdown > ul > li:nth-child(2)")
PAST_YEAR.click()

# Past month
driver.get("https://www.forbes.com/")
SEARCH_BUTTON = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header > /header > nav > div.header__right > button")
SEARCH_BUTTON.click()
SEARCH_INPUT = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header >div.search-modal > form > input")
SEARCH_INPUT.send_keys("Bangladesh")
SEARCH_INPUT.send_keys(Keys.RETURN)
PAST_MONTH = (By.CSS_SELECTOR, "body > div.main-content.main-content--overflow-visible.main-content--universal-header > main > div.search-content-wrapper > div.search-content.main-content__left-col > div.search-sort > div.search-sort__dropdown > ul > li:nth-child(3)")
PAST_MONTH.click()

# Past Week
driver.get("https://www.forbes.com/")
SEARCH_BUTTON = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header > /header > nav > div.header__right > button")
SEARCH_BUTTON.click()
SEARCH_INPUT = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header >div.search-modal > form > input")
SEARCH_INPUT.send_keys("Bangladesh")
SEARCH_INPUT.send_keys(Keys.RETURN)
PAST_WEEK = (By.CSS_SELECTOR, "body > div.main-content.main-content--overflow-visible.main-content--universal-header > main > div.search-content-wrapper > div.search-content.main-content__left-col > div.search-sort > div.search-sort__dropdown > ul > li:nth-child(4)")
PAST_WEEK.click()

# Today
driver.get("https://www.forbes.com/")
SEARCH_BUTTON = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header > /header > nav > div.header__right > button")
SEARCH_BUTTON.click()
SEARCH_INPUT = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header >div.search-modal > form > input")
SEARCH_INPUT.send_keys("Bangladesh")
SEARCH_INPUT.send_keys(Keys.RETURN)
TODAY = (By.CSS_SELECTOR,"body > div.main-content.main-content--overflow-visible.main-content--universal-header > main > div.search-content-wrapper > div.search-content.main-content__left-col > div.search-sort > div.search-sort__dropdown > ul > li:nth-child(5)")
TODAY.click()



# Close Driver
driver.close()
driver.quit()
print("Test Passed")
