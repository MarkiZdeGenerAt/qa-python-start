import pytest
from playwright.sync_api import Page, expect

def test_complete_purchase(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("Test")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("Test")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("1212")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()

    success_msg = page.locator(".complete-header")
    expect(success_msg).to_have_text("Thank you for your order!")
