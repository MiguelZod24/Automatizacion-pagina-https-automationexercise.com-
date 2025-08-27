from playwright.sync_api import Page, expect

def validar_campo_texto(page: Page, selector: str, valor: str, obligatorio: bool = True):
    campo = page.locator(selector)
    expect(campo).to_be_visible()
    if obligatorio:
        assert campo.input_value() == "", f"El campo '{selector}' no está vacío al inicio."
    campo.fill(valor)
    assert campo.input_value() == valor, f"No se llenó correctamente el campo '{selector}'"

def validar_seleccionar_checkbox(page: Page, selector: str):
    elemento = page.locator(selector)
    expect(elemento).to_be_visible()
    assert not elemento.is_checked(), f"El checkbox '{selector}' ya está seleccionado."
    elemento.check()
    assert elemento.is_checked(), f"No se pudo seleccionar el checkbox '{selector}'"

def validar_llenar_password(page: Page, selector: str, password: str):
    campo = page.locator(selector)
    expect(campo).to_be_visible()
    assert campo.input_value() == "", f"El campo '{selector}' no está vacío al inicio."
    campo.fill(password)
    assert campo.input_value() == password, f"No se llenó correctamente el campo '{selector}'"

def seleccionar_fecha(page: Page, selector_dia: str, dia: str, selector_mes: str, mes: str, selector_anio: str, anio: str):
    page.select_option(selector_dia, dia)
    page.select_option(selector_mes, mes)
    page.select_option(selector_anio, anio)

# Pasarela de pagos con tarjetas:
def validar_campo_vacio_y_llenado(page: Page, selector: str, valor: str):
    campo = page.locator(selector)
    expect(campo).to_be_visible()
    assert campo.input_value() == "", f"El campo '{selector}' no está vacío inicialmente"
    campo.fill(valor)
    assert campo.input_value() == valor, f"El campo '{selector}' no se llenó correctamente"

def agregar_producto(page, xpath_producto):
    
    #Hace hover sobre el producto usando su XPath y lo agrega al carrito.
    page.hover(xpath_producto)
    boton = page.locator(f"{xpath_producto}//div[@class='product-overlay']//i[@class='fa fa-shopping-cart']")
    boton.wait_for(state="visible")
    boton.click()

