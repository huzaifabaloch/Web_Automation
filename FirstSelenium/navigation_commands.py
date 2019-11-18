from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

'''
    Navigation commands to move forward and backward on current focused broswer.
'''

driver = webdriver.Chrome(executable_path=r'C:\Users\sunny ahmed\Desktop\Web Automation\drivers\chromedriver.exe')
driver.maximize_window()

driver.get('http://newtours.demoaut.com/')   # first url to open
print(driver.title)

driver.get('http://demo.automationtesting.in/Windows.html')  # second url to open
sleep(5)
print(driver.title)

driver.back()  # navigation
sleep(5)
print(driver.title)

driver.forward()   # navigation
sleep(5)
print(driver.title)

driver.close()

