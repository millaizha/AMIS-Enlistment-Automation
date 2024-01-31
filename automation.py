import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException


o = webdriver.ChromeOptions()
o.add_experimental_option('detach', True)
o.add_experimental_option("excludeSwitches", ["enable-automation"])
o.add_experimental_option('useAutomationExtension', False)
o.add_argument('--disable-blink-features=AutomationControlled')

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=o)

amis_url = 'https://amis.uplb.edu.ph/student/enrollment'

driver.get(amis_url)
driver.maximize_window()
driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled":True})

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bg-red-700"))).click()

print("Log in to your account", end='')
while (driver.title == 'Sign in - Google Accounts'):
    time.sleep(1)
    print('.', end='')

while (True):
    print()
    if driver.title != 'UPLB AMIS':
        driver.get(amis_url)
    else:
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-blue-500:nth-child(4)"))).click()
            if (WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(4)"))).is_displayed()):
                print('Nothing to Enlist')
                break
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pb-3 > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)"))).click()
            if (WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(4)"))).is_displayed()):
                print('Check Enlistment Warning/s')
                break
        except TimeoutException:
            continue
        



