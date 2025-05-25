import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rera.odisha.gov.in/offlineApplicationStatus")

time.sleep(5)

headers = [th.text.strip() for th in driver.find_elements(By.CSS_SELECTOR, "table thead th")]

rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")[:6]

for i, row in enumerate(rows, 1):
    cols = row.find_elements(By.TAG_NAME, "td")
    data = [col.text.strip() for col in cols]
    print(f"Project {i}:")
    for header, value in zip(headers, data):
        print(f"  {header}: {value}")
    print()

driver.quit()
