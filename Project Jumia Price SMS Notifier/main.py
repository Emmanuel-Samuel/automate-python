# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 21/03/2023
# REVISED DATE: 21/03/2023
# PURPOSE: Create Project Jumia Price SMS Notifier


# import modules
from selenium import webdriver
from twilio.rest import Client
import time

def collect_driver():
    # options class for webdriver
    options = webdriver.ChromeOptions()
    # disable info bars
    options.add_argument("disable-infobars")
    # obtains the optimal form of web page
    options.add_argument("start-maximized")
    # to avoid issues running on linux os
    options.add_argument("disable=dev=shm=usage")
    # to make sure our script has more privilege
    options.add_argument("no-sandbox")
    # to bypass the not all webpages accept this script
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    # provide path for chrome web driver
    driver = webdriver.Chrome(service=service, options=options)
    # gets the url
    driver.get("https://www.amazon.com/PlayStation-PS5-Console-Ragnar%C3%B6k-Bundle-5/dp/B0BHC395WW/ref=sr_1_3?keywords=ps5&qid=1679524552&sr=8-3")
    return driver

def main():
    driver = collect_driver()
    element = driver.find_element(by="xpath", value=""/html/body/div[1]/div[2]/div[7]/div[6]/div[4]/div[9]/div[3]/div[1]/span/span[2]/span[2]"")
    return element.text

def clean_price(raw):
    return float(raw.replace('$', ''))


account_sid = ['TWILIO_ACCOUNT_SID']
auth_token = ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

raw_price = main()
price = clean_price(raw_price)

prices = [price]

while True:
    time.sleep(10)
    raw_price = main()
    price = clean_price(raw_price)
    price.append(price)
    if prices[-1] > prices[-2]:
        message = client.messages
            .create(
                body="Hey, do know the price has pumped."
                from_ = '+11111',
                to = '+11111'
                )
    del prices[-2]

