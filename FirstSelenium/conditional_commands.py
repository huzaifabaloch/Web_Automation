from selenium import webdriver
from selenium.webdriver.common.keys import Keys


'''
    to check status of any tool in the web like checkboxes, radiobuttons, 
    buttons etc.
    1. is_displayed()  any tool
    2. is_enabled()     any tool
    3. is_selected()  -> checkboxes and radio buttons
''' 

driver = webdriver.Chrome(executable_path=r'C:\Users\sunny ahmed\Desktop\Web Automation\drivers\chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
driver.maximize_window()

user_element = driver.find_element_by_name('userName')
print(user_element.is_displayed())   # returns true or false
print(user_element.is_enabled())     # returns true or false

pass_element = driver.find_element_by_name('password')
print(pass_element.is_displayed())
print(pass_element.is_enabled())

# sending keys to input
user_element.send_keys('tuna')  
pass_element.send_keys('abc123')

driver.find_element_by_name('login').click()

round_trip = driver.find_element_by_css_selector('input[value=roundtrip]')

# print the status of radio button 
print('Status of round trip radio button: ' + str(round_trip.is_selected()))

one_way = driver.find_element_by_css_selector('input[value=oneway]')
print('Status of one way radio button: ' + str(one_way.is_selected()))
