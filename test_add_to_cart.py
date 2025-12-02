import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage  # Кирпичик 1
from pages.inventory_page import InventoryPage  # Кирпичик 2


def test_add_backpack(page: Page):
    # 1. Инициализируем страницы
    login_p = LoginPage(page)
    inventory_p = InventoryPage(page)

    # 2. Сценарий (читается как рассказ)
    login_p.navigate()
    login_p.login("standard_user", "secret_sauce")

    # Мы уже внутри! Теперь работает InventoryPage
    inventory_p.add_backpack()

    # 3. Проверка
    inventory_p.expect_items_in_cart(1)