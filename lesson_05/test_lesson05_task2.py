from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FORM_URL = "https://httpbin.qa-territory.online/forms/post"


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get(FORM_URL)

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Анастасия")

    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit order']"
    )
    submit_button.click()

    WebDriverWait(driver, 30).until(EC.url_changes(FORM_URL))
    assert driver.current_url == "https://httpbin.qa-territory.online/post"

    driver.quit()
