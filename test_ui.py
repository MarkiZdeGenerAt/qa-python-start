import pytest
from playwright.sync_api import Page, expect


# Магия: мы передаем в функцию аргумент 'page'.
# Pytest-playwright сам поймет, что нужно открыть браузер.
def test_saucedemo_login(page: Page):
    # 1. Открываем сайт
    page.goto("https://www.saucedemo.com/")

    # 2. Ищем поле по плейсхолдеру и вводим текст
    # (Это современный способ поиска элементов - не по ID, а как видит пользователь)
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    # 3. Нажимаем кнопку Логин (ищем по тексту или ID)
    page.locator("#login-button").click()

    # 4. Проверка (Assert)
    # Проверяем, что заголовок "Products" виден на странице
    heading = page.locator(".title")
    expect(heading).to_have_text("Products")
