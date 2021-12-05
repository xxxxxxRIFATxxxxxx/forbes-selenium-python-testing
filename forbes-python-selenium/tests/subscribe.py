from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup Driver
driver = webdriver.Chrome(executable_path="E:/Programming Hero/Projects/forbes-selenium-python-testing/drivers/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

# Test
driver.get("https://www.forbes.com/")

SUBSCRIBE_BUTTON = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div[4]/div/a")
SUBSCRIBE_BUTTON.click()
driver.get("https://account.forbes.com/subscribe?eventSource=header&redirect=https://www.forbes.com/home_asia/")

# Close Driver
driver.close()
driver.quit()
print("Test Passed")
