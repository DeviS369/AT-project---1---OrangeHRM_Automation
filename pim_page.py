# pages/pim_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, '''//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span''')
        self.add_employee_btn = (By.XPATH, '''//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button''')
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")
        self.save_button = (By.XPATH, '''//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]''')
    
    def go_to_pim_module(self):
        self.driver.find_element(*self.pim_menu).click()

    def add_employee(self, first_name, last_name):
        self.driver.find_element(*self.add_employee_btn).click()
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()
