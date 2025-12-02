from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # Локаторы
        self.backpack_add_btn = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.menu_button = page.locator("#react-burger-menu-btn")

    # Действие: Добавить рюкзак
    def add_backpack(self):
        self.backpack_add_btn.click()

    # Проверка: Убедиться, что на значке корзины цифра 1
    def expect_items_in_cart(self, count):
        expect(self.cart_badge).to_have_text(str(count))