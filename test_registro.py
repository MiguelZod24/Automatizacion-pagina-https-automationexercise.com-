import random
import pytest
import time
from playwright.sync_api import Page, expect
from helpers import validar_campo_texto, validar_seleccionar_checkbox, validar_llenar_password, seleccionar_fecha

def generar_email_aleatorio() -> str:
    numero = random.randint(1000, 9999)
    return f"migue{numero}@test.com"

@pytest.mark.registro
def test_registro_usuario_exitoso(page: Page):
    page.goto("https://automationexercise.com/")
    expect(page).to_have_url("https://automationexercise.com/")

    cookie_button = page.locator("div[class='fc-dialog-container'] button.fc-cta-consent")
    if cookie_button.is_visible():
        cookie_button.click()

    page.click("a[href='/login']")
    expect(page).to_have_url("https://automationexercise.com/login")

    nombre = "Migue Tester"
    email = generar_email_aleatorio()

    page.fill("input[data-qa='signup-name']", nombre)
    page.fill("input[data-qa='signup-email']", email)
    page.click("button[data-qa='signup-button']")

    expect(page.get_by_text("Enter Account Information")).to_be_visible()

    validar_seleccionar_checkbox(page, "#id_gender1")
    validar_llenar_password(page, "#password", "ClaveSegura123")
    seleccionar_fecha(page, "#days", "7", "#months", "8", "#years", "1990")

    page.check("#newsletter")
    page.check("#optin")

    validar_campo_texto(page, "#first_name", "Migue")
    validar_campo_texto(page, "#last_name", "QA")
    validar_campo_texto(page, "#company", "QA Corp")
    validar_campo_texto(page, "#address1", "Calle Falsa 123")
    validar_campo_texto(page, "#address2", "Otra Calle")
    validar_campo_texto(page, "#state", "Ontario")
    validar_campo_texto(page, "#city", "Toronto")
    validar_campo_texto(page, "#zipcode", "M4B1B3")
    validar_campo_texto(page, "#mobile_number", "+123456789")

    page.click("button[data-qa='create-account']")
    expect(page.locator("b")).to_have_text("Account Created!")

    page.click("a[data-qa='continue-button']")
    expect(page.locator("a", has_text=f"Logged in as {nombre}")).to_be_visible()
    
    time.sleep(3)

    page.click("a[href='/logout']")
    expect(page).to_have_url("https://automationexercise.com/login")

    time.sleep(3)


