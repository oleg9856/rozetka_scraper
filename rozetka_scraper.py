from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Correct path to the ChromeDriver executable
driver_path = os.environ['DRIVER_PATH']

# URL of the page with monitors
url = "https://rozetka.com.ua/ua/search/?text=monitor"

# Create an instance of ChromeOptions
options = Options()

# Create a Service object with the correct path to the ChromeDriver
service = Service(driver_path)

# Create an instance of the Chrome WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)

# Open the page
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Load the page source into BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the relevant HTML elements that contain the item information
items = soup.find_all('div', class_='goods-tile__inner')

# Extract and print the item details
for item in items:
    title = item.find('a', class_='goods-tile__heading').text.strip()
    price = item.find('span', class_='goods-tile__price-value').text.strip()
    print(f'Title: {title}, Price: {price}')

# Close the browser
driver.quit()