import pytest
from playwright.sync_api import Page, expect
# Импортируем наш новый класс страницы
from pages.login_page import LoginPage


def test_login_with_pom(page: Page):
    # 1. Создаем объект страницы
    login_p = LoginPage(page)

    # 2. Используем методы страницы (читается как инструкция)
    login_p.navigate()
    login_p.login("standard_user", "secret_sauce")

    # 3. Проверка (остается в тесте!)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")