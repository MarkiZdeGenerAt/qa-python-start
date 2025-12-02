from playwright.sync_api import Page

class LoginPage:
    # Конструктор: когда мы создаем страницу, мы даем ей "браузер" (page)
    def __init__(self, page: Page):
        self.page = page
        # Локаторы (адреса элементов) храним здесь
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")

    # Действие: Открыть страницу
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    # Действие: Залогиниться
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()