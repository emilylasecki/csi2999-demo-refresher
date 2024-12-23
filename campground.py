import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

service = Service(executable_path="C:\Program Files\chromedriver-win32\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://csi-2999-project.onrender.com/reservations")
request = requests.get("https://csi-2999-project.onrender.com/reservations")

print(requests)

soup = BeautifulSoup(request.content, 'html.parser')
print(soup.prettify())

# ActionChains(options).click(element).perform()