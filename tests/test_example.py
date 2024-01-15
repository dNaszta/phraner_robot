'''
This is an example of a test script that uses Selenium to test a web page that contains a popup element
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
# use this option for running browser without profile
options.add_argument("--user-data-dir=/dev/null")

# create a new Edge session
driver = webdriver.Edge(options=options)
driver.get('https://getbootstrap.com/docs/5.0/getting-started/introduction/')

try:
    # locate the button and click it
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bd-versions"))
    )
    button.click()

    # wait for the popup element to be loaded
    # replace 'your_popup_element_id' with the actual ID of your popup element
    popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.dropdown-menu-end.show"))
    )

    # check if the popup contains the text "All versions"
    if "All versions" in popup.text:
        print("Text 'All versions' found in the popup")
    else:
        print("Text 'All versions' not found in the popup")
finally:
    # close the browser window
    driver.quit()
