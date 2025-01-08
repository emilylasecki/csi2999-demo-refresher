import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time as tyme
from selenium.webdriver.common.by import By
from datetime import datetime, time, timedelta
from pathlib import Path

def createNewEntry():
    service = Service(executable_path="C:\Program Files\chromedriver-win32\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://csi-2999-project.onrender.com/reservations")
    request = requests.get("https://csi-2999-project.onrender.com/reservations")

    soup = BeautifulSoup(request.content, 'html.parser')

    button = driver.find_element("id", "dateRange")
    button.click()

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

   # tyme.sleep(5)



# get today's date
today = datetime.today().date()


# get date last run from file in home directory
home_dir = Path.home()
path = home_dir / "dateRefresherLastRun.txt"
f = open(path, 'r')
content=f.read()

format = '%Y-%m-%d'
f.close()

lastRun = datetime.strptime(content, format).date()
fourDaysLater = lastRun + timedelta(days=4)

if fourDaysLater < today: # if script hasn't been run in the last 4 days, run it
    createNewEntry()

    wr = open(path, 'w')
    text = today.strftime(format)
    wr.write(text)
    wr.close()



