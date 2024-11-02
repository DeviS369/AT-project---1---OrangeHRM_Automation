# pages/pim_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.ID, "menu_pim_viewPimModule")
        self.add_employee_btn = (By.ID, "btnAdd")
        self.first_name_field = (By.ID, "firstName")
        self.last_name_field = (By.ID, "lastName")
        self.save_button = (By.ID, "btnSave")
    
    def go_to_pim_module(self):
        self.driver.find_element(*self.pim_menu).click()

    def add_employee(self, first_name, last_name):
        self.driver.find_element(*self.add_employee_btn).click()
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()
