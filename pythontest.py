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


text = driver.find_element(By.XPATH,"/html/body/div[20]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/section/div[2]/div[2]/div[1]/div/span").text

print(text)


driver.get("https://www.stats.gov.sa/ar/job-details/" + text)


input("اضغط أي مفتاح لإغلاق المتصفح...")
driver.quit()