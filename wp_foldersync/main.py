#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the URL of the WordPress admin login page
admin_url = "https://fabienne-martin.ch/wp-admin/admin.php?page=nggallery-manage-gallery&mode=edit&gid=1&paged=1"

# Set your WordPress admin credentials
username = "dokagimo"
password = "w5eCQXwCCy!"

# Initialize the Firefox driver
driver = webdriver.Firefox()

try:
    # Navigate to the WordPress admin login page
    driver.get(admin_url)

    # Find the username and password input fields
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user_login"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user_pass"))
    )

    # Enter your WordPress admin username and password
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Find and click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wp-submit"))
    )
    login_button.click()

    time.sleep(10)

    # Locate the <span> element with the class "toggle-indicator"
    toggle_indicator = driver.find_element(
        By.CSS_SELECTOR, "span.toggle-indicator")

    # Click on the <span> element to simulate a button click
    toggle_indicator.click()

    time.sleep(10)

    # Find the button element by CSS selector and click it
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             'input[type="submit"].button-primary[name="scanfolder"][value="Scan Folder for new images"]')
        )
    )
    button.click()


finally:
    # Close the browser when done
    driver.quit()
