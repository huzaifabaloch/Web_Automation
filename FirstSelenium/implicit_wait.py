from selenium import webdriver
from selenium.webdriver.common.keys import Keys


'''
    Wait for all the elements to display on page.
'''

driver = webdriver.Chrome(executable_path=r'C:\Users\sunny ahmed\Desktop\Web Automation\drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://newtours.demoaut.com/')

# wait some time here to load the entire page content like
# 1. wait for all the elements to display. 
# 2. some elements might  take some time so it will wait until loads all the 
# elements are displayed 
# 3. only one time to use in the beginning of the page.
driver.implicitly_wait(10)

assert 'Welcome: Mercury Tours' in driver.title

driver.find_element_by_name('userName').send_keys('tuna')
driver.find_element_by_name('password').send_keys('abc123')

driver.find_element_by_name('login').click()
driver.close()