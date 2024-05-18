from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&ifkv=ASKXGp3Cgd2e0Mp65nAiNEGuAOhUFejcCs43d3_1Z-jsdNRUnHVI5LDNWAkLv3Xz-1rlUtBd03CD&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1862435316%3A1703657709035915&theme=glif")

driver.find_element("xpath", "//input[@id='identifierId']").send_keys("mgirjapure@awengworks.com")
driver.find_element("xpath", "//span[normalize-space()='Next']").click()
sleep(5)
driver.find_element("xpath", "//input[@name='Passwd']").send_keys("Aweng@2021")
driver.find_element("xpath", "//span[normalize-space()='Next']").click()
sleep(5)
driver.quit()
