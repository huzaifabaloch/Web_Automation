from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r'C:\Users\sunny ahmed\Desktop\Web Automation\drivers\chromedriver.exe')
#driver = webdriver.Ie(r'C:\Users\sunny ahmed\Desktop\Web Automation\drivers\IEDriverServer.exe')

driver.get('http://newtours.demoaut.com/')
print(driver.title) # Title of webpage
print(driver.current_url)  # url of the webpage
print(driver.page_source)  # returns the html code of the webpage.
driver.close()  # Close the web browser