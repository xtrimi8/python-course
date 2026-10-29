# python-course

# Как запустить тесты и посмотреть отчёт

# 1. Установка зависимостей
pip install pytest selenium allure-pytest

# 2. Запуск тестов с Allure
pytest lesson_10 --alluredir=allure-results

# 3. Просмотр отчёта
allure serve allure-results

# 4. Генерация статического отчёта
allure generate allure-results -o allure-report --clean
