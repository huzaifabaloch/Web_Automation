from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


# Using chrome browser
driver = webdriver.Chrome(r'C:\Users\sunny ahmed\Desktop\Web Automation\drivers\chromedriver.exe')

driver.get('http://demo.automationtesting.in/Windows.html')
print(driver.title)  # title of the page.
print(driver.current_url)  # url of the page.

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
sleep(5)


driver.close()   # closes the current focused browser
driver.quit()   # close all the browsers
