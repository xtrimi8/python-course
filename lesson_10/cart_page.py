from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self) -> None:
        """Нажимает кнопку Checkout в корзине."""
        self.driver.find_element(By.ID, "checkout").click()
