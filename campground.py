import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Program Files\chromedriver-win32\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://csi-2999-project.onrender.com/reservations")
request = requests.get("https://csi-2999-project.onrender.com/reservations")

print(requests)

soup = BeautifulSoup(request.content, 'html.parser')
#print(soup.prettify())

button = driver.find_element("id", "dateRange")
button.click()
#time.sleep(5)

#soup = BeautifulSoup(request.content, 'html.parser')
#print(soup.prettify)

nextmonth = driver.find_element(By.CLASS_NAME, "flatpickr-next-month")

nextmonth.click()

chooseday = driver.find_element(By.CLASS_NAME, "dayContainer")
chooseday.click()

chooseday2 = driver.find_element(By.CLASS_NAME, "flatpickr-day.nextMonthDay")
chooseday2.click()

clicksubmit = driver.find_element(By.CLASS_NAME, "block")
clicksubmit.click()

choosesite = driver.find_element(By.CLASS_NAME, "selectBtn")
choosesite.click()

firstname = driver.find_element(By.ID, "first-name")
firstname.click()

firstname.send_keys("test first name")

lastname = driver.find_element(By.ID, "last-name")
lastname.click()
lastname.send_keys("test last name")

email = driver.find_element(By.ID, "email")
email.click()
email.send_keys("fakeemail@email.com")

phone = driver.find_element(By.ID, "phone")
phone.click()
phone.send_keys("1234567890")

terms = driver.find_element(By.ID, "agreed-to-terms")
terms.click()

submit = driver.find_element(By.ID, "reservation-submit-btn")
submit.click()

time.sleep(5)

# ActionChains(options).click(element).perform()