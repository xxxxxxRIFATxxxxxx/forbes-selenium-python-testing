from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup Driver
driver = webdriver.Chrome(executable_path="E:/Programming Hero/Projects/forbes-selenium-python-testing/drivers/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

# Test
driver.get("https://www.forbes.com/")

SIGN_IN_BUTTON = driver.find_element(By.CSS_SELECTOR, "body > div.main-content.main-content--universal-header > header > nav > div.header__right > div > div")
SIGN_IN_BUTTON.click()

# Close Driver
driver.close()
driver.quit()
print("Test Passed")
