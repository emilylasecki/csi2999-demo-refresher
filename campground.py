from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from pathlib import Path
import sys
import os

def resource_path(relative_path):  # configure so pyinstaller can read path names
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def createNewEntry():
    exe_path=resource_path("C:\Program Files\chromedriver-win32\chromedriver.exe")
    service = Service(executable_path=exe_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://csi-2999-project.onrender.com/reservations")

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

# get today's date
today = datetime.today().date()

# get date last run from file in home directory
home_dir = resource_path(Path.home())
path = resource_path(Path.home() / "dateRefresherLastRun.txt")
f = open(path, 'r')
content=f.read()

format = '%Y-%m-%d'
f.close()

lastRun = datetime.strptime(content, format).date()
fourDaysLater = lastRun + timedelta(days=3)

if fourDaysLater < today: # if script hasn't been run in the last 4 days, run it
    createNewEntry()

    wr = open(path, 'w')
    text = today.strftime(format)
    wr.write(text)
    wr.close()



