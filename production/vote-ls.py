# ##################################
# Program: vote-ls.py
# python3.6+
# Name: Populate google forms example
# Description: This code use selenium google driver to populate fields/checkbox in a google form
# versão: 1
# Dependencies: selenium / webdriver google chrome
# Created: 08/28/2019 
# Last Modified: 10/28/2019
# ##################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def checkVisiblebyClass(toDriver, time, el_class):
    WebDriverWait(toDriver, time).until(
        EC.visibility_of_element_located((By.CLASS_NAME, el_class))
    )

driver = webdriver.Chrome(executable_path="/usr/local/lib/python3.6/dist-packages/selenium/webdriver/chrome/chromedriver")  # Optional argument, if not specified will search path.
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSd_uLoxPbBr68HeeKXDIM7jkvxg-oNDYJtNtozotNKhSRwcvQ/viewform?usp=sf_link')
EMAILS = ["0@gmail.com", "1@gmail.com", "2@gmail.com", "3@gmail.com", "4@gmail.com"]

for i in EMAILS:
    INPUT_EMAIL = driver.find_element_by_name("emailAddress")
    checkVisiblebyClass(driver, 30, 'quantumWizTextinputPaperinputInputArea')
    INPUT_EMAIL.send_keys(i)
    driver.find_element_by_class_name("freebirdFormviewerViewNavigationNoSubmitButton").click()
    checkVisiblebyClass(driver, 30, 'quantumWizTogglePaperradioEl')
    button = driver.find_elements_by_class_name('quantumWizTogglePaperradioEl')
    for j in button:
        sel = j.get_attribute('data-value')
        if sel == "Campea":
            j.click()
            checkVisiblebyClass(driver, 30, 'freebirdFormviewerViewNavigationSubmitButton')
            driver.find_element_by_class_name('freebirdFormviewerViewNavigationSubmitButton').click()
            break
    checkVisiblebyClass(driver, 30, 'freebirdFormviewerViewResponseLinksContainer')
    Next = driver.find_element_by_class_name("freebirdFormviewerViewResponseLinksContainer")
    Next.find_element_by_tag_name("a").click()
    checkVisiblebyClass(driver, 30, 'quantumWizTextinputPaperinputInputArea')
    continue
