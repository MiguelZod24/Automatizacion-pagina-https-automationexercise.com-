import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page, Playwright

@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=100)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def usuario_registrado():
    return {
        "email": "cualquiera@test.com",  # correo ya existente en la página
        "password": "123456"
    }

