from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        """Открывает страницу авторизации."""
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """Вводит логин и пароль, нажимает кнопку входа."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
