from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
 
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.appsheet.com/start/cc3a5a86-a592-40c4-98cd-807f9bc91b1d")

another1_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[4]/div/div/div[2]/div/div[2]/button[2]/span[1]"))
)
another1_button.click()
time.sleep(5)

another3_button = WebDriverWait(driver, 5000).until(
EC.presence_of_element_located((By.XPATH,"/html/body/div[15]/div[3]/div/div/button"))
)
driver.execute_script("arguments[0].click();", another3_button)
time.sleep(2)

another4_button = WebDriverWait(driver, 5000).until(
EC.element_to_be_clickable((By.XPATH,"/html/body/div[19]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/span[1]/div[2]/div/div[1]/div/div/span"))
)
another4_button.click()
time.sleep(2)


code = driver.find_element(By.XPATH,"/html/body/div[20]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/section/div[2]/div[2]/div[1]/div/span").text

print(code)


driver.get("https://www.stats.gov.sa/ar/job-details/" + code)

name = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div[1]/div[3]/div[3]/div/section/div/div/div/div[1]/h1/span").text
description = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div[1]/div[3]/div[3]/div/section/div/div/div/div[2]/div").text


driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeQn7RWmdhhpD_a6_HbnFf8qtN4LrLZkXtj7ExXoR-RCmnseA/viewform")


input_code = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"))
    )
input_code.send_keys(code)



input_description = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea"))
    )
input_description.send_keys(description)

print(input2)
print(name)
print(description)

input("اضغط أي مفتاح لإغلاق المتصفح...")
driver.quit()