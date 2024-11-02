# conftest.py
import pytest
from selenium import webdriver
from datetime import datetime

@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            screenshot_name = f"screenshots/{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            driver.save_screenshot(screenshot_name)
