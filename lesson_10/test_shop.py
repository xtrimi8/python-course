import allure
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.title("Проверка покупки в магазине")
@allure.description("Тест проверяет полный цикл покупки")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Firefox()
    try:
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открыть сайт и авторизоваться"):
            login_page.open()
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить три товара в корзину"):
            main_page.add_to_cart("sauce-labs-backpack")
            main_page.add_to_cart("sauce-labs-bolt-t-shirt")
            main_page.add_to_cart("sauce-labs-onesie")

        with allure.step("Перейти в корзину"):
            main_page.go_to_cart()

        with allure.step("Нажать Checkout"):
            cart_page.checkout()

        with allure.step("Заполнить форму"):
            checkout_page.fill_form("Анастасия", "Котовская", "123456")

        with allure.step("Проверить итоговую сумму"):
            total = checkout_page.get_total()
            assert "$58.29" in total

    finally:
        driver.quit()
