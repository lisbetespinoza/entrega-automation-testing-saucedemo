from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.reader import read_productos_json
from utils.logger import logger

def test_cart(driver):
    try:
        logger.info("Inicializando prueba de carrito")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        logger.info("Ingresando a la pagina web de prueba")
        driver.get("https://www.saucedemo.com/")
             
        logger.info("Iniciando sesion con credenciales validas")             
        login_page.login("standard_user", "secret_sauce")
        logger.info("Sesion iniciada correctamente")  
        
        logger.info("Ingresando a la pagina de inventario") 
        
        logger.info("Leyendo el primer producto del JSON")
        # Leer el primer producto del JSON 
        producto = read_productos_json()[0]
        print(producto)
        
        logger.info("Agregando producto del JSON al carrito")
        # Agregar producto del JSON
        inventory_page.agregar_producto(producto["nombre"])
        
        assert inventory_page.obtener_contador_carrito() == "1"
        logger.info("Prueba de contador de carrito validada")
        
        logger.info("Ir a la pagina del carrito")
        # Ir al carrito
        inventory_page.ir_al_carrito()
        
        logger.info("Prueba del nombre del producto en carrito contra el JSON validada")
        # Validar nombre contra el JSON
        assert cart_page.obtener_nombre_producto() == producto["nombre"]
        
        logger.info("Prueba del precio del producto en carrito contra el JSON validada")
        # Validar precio contra el JSON
        assert cart_page.obtener_precio_producto() == producto["precio"]
    except Exception:
        logger.exception("Error durante la prueba de carrito")       
        
        
        