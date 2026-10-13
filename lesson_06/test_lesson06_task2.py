from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cookiesBtn"))
        )
        cookie_button.click()
    except Exception:
        pass

    driver.add_cookie({
        "name": "SESSION",
        "value": "MDg3MTNjNTEtMDY4Yy00MjZkLThlYzctNmIxNzUyZDdkZDBh"
    })
    driver.add_cookie({
        "name": "X-CSRF-TOKEN",
        "value": "79619abb-6b29-4770-abc0-53c017e49257"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/anastasia_k")
    url_user1 = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": "NmU0NTc0OWMtYTQ1YS00ZWNjLTlmM2MtNmRkODQ2ZDZlYTFk"
    })
    driver.add_cookie({
        "name": "X-CSRF-TOKEN",
        "value": "ad95a482-3b06-4e27-9b67-94e8d956fe56"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/anastasia_52")
    url_user2 = driver.current_url

    assert url_user1 != url_user2

    driver.quit()
