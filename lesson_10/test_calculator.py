import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.title("Проверка калькулятора")
@allure.description("Тест проверяет работу калькулятора с задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay(45)

        with allure.step("Нажать кнопки 7, +, 8, ="):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Проверить результат"):
            result = page.get_result("15")
            assert result == "15"

    finally:
        driver.quit()
