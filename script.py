# Program to send bulk customized message through WhatsApp web application
# LOOK AT THE README FILE
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
i = 0

# Iterate excel rows till to finish
for column in excel_data['Name'].tolist():
    # Assign customized message
    message = excel_data['Message'][i]
    message = message.replace('{customer_name}', column)
    # Locate search box
    search_box = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
    person_title = wait.until(lambda driver:driver.find_element("xpath",search_box))

    # Clear search box if any contact number is written in it
    person_title.clear()

    # Send contact number in search box
    person_title.send_keys(str(excel_data['Contact'][count]))
    count = count + 1
    i = i + 1
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