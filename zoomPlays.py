from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import keypresser
import keyholder
import threading

# Capabilities
capabilities = DesiredCapabilities.FIREFOX
capabilities['loggingPrefs'] = { 'browser':'ALL'}

driver = webdriver.Firefox(desired_capabilities=capabilities)
driver.get("https://zoom.us/j/94778141102?pwd=c09LYVhzQjdqRDdCTUYyUkhmMzNQUT09")

meetingPw = 'Tt0uY5'
    
c = ''

def printThing():
    threading.Timer(1.0, printThing).start()
    print("-----------------------")
    elementName = driver.find_elements_by_class_name("chat-item__chat-info-msg")
    # print(elementName[len(elementName)-1].text)
    cz = elementName[-1].text.split("\n")
    c = cz[-1]
    print(c)

printThing()

keyholder.holdForSeconds(c, 0.3)