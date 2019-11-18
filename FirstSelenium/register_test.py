from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class RegisterUser:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\sunny ahmed\Desktop\Web Automation\drivers\chromedriver.exe')
        self.register(self.password)

    def register(self, password):
        
        self.driver.get('http://newtours.demoaut.com/mercuryregister.php')
        self.driver.maximize_window()
        email = self.driver.find_element_by_name('email')
        passwd = self.driver.find_element_by_name('password')
        confirm = self.driver.find_element_by_name('confirmPassword')
        confirm_password = password
        email.send_keys(self.user_name)
        passwd.send_keys(self.password)
        confirm.send_keys(confirm_password)
        reg = self.driver.find_element_by_name('register')
        reg.send_keys(Keys.ENTER)
        sleep(5)
        self.close_driver()

    def close_driver(self):
        self.driver.close()


acc1 = RegisterUser('toaster', 'eaton')
        
