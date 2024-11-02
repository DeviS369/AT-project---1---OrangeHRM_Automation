# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//form//button[@type='submit']")
        self.error_message = (By.ID, "spanMessage")
    
    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.error_message)
        )
        return self.driver.find_element(*self.error_message).text
