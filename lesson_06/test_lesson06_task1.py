from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#finish"), "Hello World!"
        )
    )

    hello_text = driver.find_element(By.CSS_SELECTOR, "#finish")
    driver.save_screenshot("lesson_06/dynamic_loading.png")
    assert hello_text.text == "Hello World!"

    driver.quit()
