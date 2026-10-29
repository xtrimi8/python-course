from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_id: str) -> None:
        """Добавляет товар в корзину по его id."""
        self.driver.find_element(
            By.ID, f"add-to-cart-{item_id}"
        ).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
