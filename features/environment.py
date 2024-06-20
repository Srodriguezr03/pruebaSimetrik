# Importamos
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from lib.pages.basepage import BasePage
from lib.pages.homepage import HomePage

# Función que se ejecuta antes de todos los tests
def before_all(context):
    # Inicializa el WebDriver de Selenium
    context.driver = set_selenium_driver()
    # Establece un tiempo de espera máximo para la carga de página
    context.driver.set_page_load_timeout(30)
    # Maximiza la ventana del navegador
    context.driver.maximize_window()

    # Inicializa la página base y la página de inicio con el driver y el contexto
    context.browser = BasePage(context.driver, context)
    context.home = HomePage(context.driver, context)

    # Almacena las diferentes páginas en un diccionario para fácil acceso
    contexts = {
        'home': context.home,
    }

    # Asigna el diccionario de contextos al contexto global
    context.all_contexts = contexts
    print("before_all: WebDriver initialized")

# Función que se ejecuta después de cada escenario
def after_scenario(context, scenario):
    print(f"after_scenario: Scenario {scenario.name} finished")
    pass

# Función que se ejecuta después de todos los tests
def after_all(context):
    # Verifica si el contexto tiene un atributo 'driver' y lo cierra si existe
    if hasattr(context, 'driver'):
        context.driver.quit()
        print("after_all: Test execution complete. Closing browser.")

# Función que configura e inicializa el WebDriver de Selenium
def set_selenium_driver():
    # Configura las opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    service = ChromeService(ChromeDriverManager().install())
    print("set_selenium_driver: ChromeDriver initialized with service:", service)

    # Inicializa el driver de Chrome con las opciones configuradas
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
