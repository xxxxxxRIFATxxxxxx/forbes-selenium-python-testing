from selenium import webdriver

# Setup Driver
driver = webdriver.Chrome(executable_path="E:/Programming Hero/Projects/forbes-selenium-python-testing/drivers/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

# Test
driver.get("https://www.forbes.com/")

# Close Driver
driver.close()
driver.quit()
print("Test Passed")