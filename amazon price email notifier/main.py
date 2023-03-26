# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 21/03/2023
# REVISED DATE: 21/03/2023
# PURPOSE: Create Project Amazon Price Email Notifier


# import modules
import yagmail
from selenium import webdriver
import time
import os

def collect_driver():
    # options class for webdriver
    options = webdriver.ChromeOptions()
    # disable info bars
    options.add_argument("disable-infobars")
    # obtains the optimal form of web page
    options.add_argument("start-maximized")
    # to avoid issues running on linux os
    options.add_argument("disable=dev=shm=usage")
    # to make sure our script has more priviledge
    options.add_argument("no-sandbox")
    # to bypass the not all webpages accept this script
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    # provide path for chrome web driver
    driver = webdriver.Chrome(service=service, options=options)
    # gets the url
    driver.get("https://www.amazon.com/PlayStation-PS5-Console-Ragnar%C3%B6k-Bundle-5/dp/B0BHC395WW/ref=sr_1_3?keywords=ps5&qid=1679524552&sr=8-3")
    return driver


# function to webscrape the price value of the item
def main():
    driver = collect_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/div[7]/div[6]/div[4]/div[9]/div[3]/div[1]/span/span[2]/span[2]")
    return element.text


# function to clean the price value
def clean_price(raw):
    return float(raw.replace('$', ''))


# message recipients defined
sender = "(replace with email)"
receiver = "(replace with email)"

# assigns price value to raw_price
raw_price = main()
# cleans price value
price = clean_price(raw_price)
# defines a list for holding price values
prices = [price]


# Loop for continuous running of app
while True:
    time.sleep(3600)
    raw_price = main()
    price = clean_price(raw_price)
    price.append(price)
    # checks for changes in price
    if prices[-1] > prices[-2]:
        subject = f"Price pumps to ${price}. Hurry up!"
        contents = f"""
        Hi, do you know the price has pumped to ${price}
        """
        yag = yagmail.SMTP(user=sender,
                           password=os.getenv('PASSWORD'))
        yag.send(to=receiver, subject=subject,
                 contents=contents)
        print("Sent")
    # deletes previous price so list stays updated
    del prices[-2]
