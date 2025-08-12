import pytest
from playwright.sync_api import Page, expect
import time
from helpers import validar_campo_vacio_y_llenado, agregar_producto

@pytest.mark.compra

def test_usuario_existente(page: Page, usuario_registrado):
    # Ir al sitio
    page.goto("https://automationexercise.com/")
    expect(page).to_have_url("https://automationexercise.com/")

    # Cerrar cookies si aparece
    cookie_button = page.locator("div[class='fc-dialog-container'] button.fc-cta-consent")
    if cookie_button.is_visible():
        cookie_button.click()

    # Ir a login
    page.click("a[href='/login']")
    expect(page).to_have_url("https://automationexercise.com/login")

    # Iniciar sesión
    page.fill("input[data-qa='login-email']", usuario_registrado["email"])
    page.fill("input[data-qa='login-password']", usuario_registrado["password"])
    page.click("button[data-qa='login-button']")

    # Validar login
    expect(page.locator("xpath=//a[contains(.,'Logged in as Miguel')]")).to_be_visible()

    # Ir a la página de productos
    page.click("a[href='/products']")
    expect(page).to_have_url("https://automationexercise.com/products")

    # Hacer hover sobre el producto
    # page.hover("div.features_items > div:nth-child(3)")  # Selector
    # button = page.locator("div.features_items > div:nth-child(3) div.product-overlay a.add-to-cart")
    # button.click()

    # page.get_by_role("button", name="Continue Shopping").click()

    # # Hacer hover sobre el segundo producto y añadirlo al carrito
    # page.hover("//div[@class='features_items']/div[5]")
    # page.locator("//div[@class='features_items']/div[5]//div[@class='product-overlay']//i[@class='fa fa-shopping-cart']").click()

    # page.get_by_role("button", name="Continue Shopping").click()

    # Hacer hover sobre el segundo producto y añadirlo al carrito
    # page.hover("//div[@class='features_items']/div[7]")
    # page.locator("//div[@class='features_items']/div[7]//div[@class='product-overlay']//i[@class='fa fa-shopping-cart']").click()

    # Agregar productos
    agregar_producto(page, "//div[@class='features_items']/div[3]")
    page.get_by_role("button", name="Continue Shopping").click()

    agregar_producto(page, "//div[@class='features_items']/div[5]")
    page.get_by_role("button", name="Continue Shopping").click()

    agregar_producto(page, "//div[@class='features_items']/div[7]")

    # Continuar al carrito
    page.get_by_role("link", name="View Cart").click()
    expect(page).to_have_url("https://automationexercise.com/view_cart")

    # Proceder al checkout
    page.click("a[class='btn btn-default check_out']")
    expect(page).to_have_url("https://automationexercise.com/checkout")

    # Confirmar dirección y resumen
    expect(page.locator("h2", has_text="Address Details")).to_be_visible()

    # Colocar comentario
    page.fill("textarea[name='message']", "Por favor, entregar rápido")
    page.click("a[class='btn btn-default check_out']")

    # Pago con validaciones
    validar_campo_vacio_y_llenado(page, "input[name='name_on_card']", "Migue Tester")
    validar_campo_vacio_y_llenado(page, "input[name='card_number']", "4111111111111111")
    validar_campo_vacio_y_llenado(page, "input[name='cvc']", "123")
    validar_campo_vacio_y_llenado(page, "input[name='expiry_month']", "12")
    validar_campo_vacio_y_llenado(page, "input[name='expiry_year']", "2025")

    page.click("#submit")
    
    # Validar confirmación
    expect(page.get_by_text("Order Placed!")).to_be_visible()

    time.sleep(5)  # Pausa para ver el final antes de cerrar
