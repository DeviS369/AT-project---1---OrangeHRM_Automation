# tests/test_pim.py
import pytest
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

@pytest.mark.usefixtures("setup")
class TestPIM:
    def test_add_employee(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        pim_page = PIMPage(self.driver)
        pim_page.go_to_pim_module()
        pim_page.add_employee("John", "Doe")
        
        # Assuming success message element
        assert "Successfully Saved" in self.driver.page_source, "Employee addition failed."
