# Python Automated Bulk WhatsApp Messages

It is a python script that sends WhatsApp message automatically from WhatsApp web application with saved contact numbers. It can be configured to send advertising messages to customers. It read data from an excel sheet and send a configured message to people.

## Note
This is for saved contact numbers only if you want to send whatsapp bulk messages to unsaved or without saving the contact numbers. 

## Prerequisites

In order to run the python script, your system must have the following programs/packages installed and the contact number should be saved in your phone (You can use bulk contact number saving procedure of email). There is a way without saving the contact number but has the limitation to send the attachment.
* Latest Python : Download it from https://www.python.org/downloads
* Selenium Web Driver: Either you can use repo driver else you can download it https://chromedriver.chromium.org/downloads
* Google Chrome : Download it from https://www.google.com/chrome
* Pandas : Run in command prompt **pip install pandas**
* Xlrd : Run in command prompt **pip install xlrd**
* Selenium: Run in command prompt **pip install selenium** 


## Approach
* User scans web QR code to log in into the WhatsApp web application.
* The script reads a customized message from excel sheet.
* The script reads rows one by one and searches that contact number in the web search box if the contact number found on WhatsApp then it will send a configured message otherwise It reads next row. 
* Loop execute until and unless all rows complete.

Note: If you wish to send an image instead of text you can write attachment selection python code.

## Legal
* This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk. Commercial use of this code/repo is strictly prohibited.

## Code
```
# Program to send bulk customized message through WhatsApp web application
# Author @TalNaeh007

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pandas
import time

# Load the chrome driver
driver = webdriver.Chrome()
count = 0

# Open WhatsApp URL in chrome browser
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
# Wait until page is completly loaded
time.sleep(50)

wait = WebDriverWait(driver, 30)


# Read data from excel
excel_data = pandas.read_excel(r'/Users/tnaeh/Downloads/python-automated-bulk-whatsapp-messages-master/python-automated-bulk-whatsapp-messages-master/Customer bulk email data.xlsx', sheet_name='Customers')


# Iterate excel rows till to finish
for column in excel_data['Name'].tolist():
    # Assign customized message
    message = excel_data['Message'][0]
    message = message.replace('{customer_name}', column)


    # Locate search box
    search_box = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
    person_title = wait.until(lambda driver:driver.find_element("xpath",search_box))

    # Clear search box if any contact number is written in it
    person_title.clear()

    # Send contact number in search box
    person_title.send_keys(str(excel_data['Contact'][count]))
    count = count + 1
    person_title.send_keys(Keys.ENTER)

    # Wait for 2 seconds to search contact number
    time.sleep(2)

    # Send message content in chat box
    chat_bar = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    chat_bar_element = wait.until(lambda driver:driver.find_element("xpath",chat_bar))
    chat_bar_element.click()
    chat_bar_element.send_keys(message)

    # Wait for 3 seconds to search contact number
    time.sleep(3)

    # Locate and press the send button
    send_button = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'
    wait.until(lambda driver:driver.find_element("xpath",send_button)).click()

    # Wait for 3 seconds before moving on to the next iteration
    time.sleep(3)

# Close chrome browser
driver.quit()