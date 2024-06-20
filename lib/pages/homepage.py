# Importamos
import logging
from lib.components.generalcomponents import GeneralComponents
from lib.helpers.generalhelpers import validate_wait_results
from lib.pages.basepage import BasePage
from lib.pages.webelements.homewebelements import HomeWebElements

# Configuramos el logger para la clase HomePage
logger = logging.getLogger(__name__)

# Definimos la clase HomePage que hereda de BasePage
class HomePage(BasePage):
    def __init__(self, driver, context):
        # Inicializamos la clase base con el driver y el contexto
        super().__init__(driver, context)
        # Asignamos los elementos web específicos de la página de inicio
        self.webElements = HomeWebElements

    # Método para verificar si la página está abierta
    def is_open(self):
        return validate_wait_results(
            # Esperamos hasta que el elemento 'where_label' esté presente en la página
            GeneralComponents.wait_until_element_is_present(self.driver, HomeWebElements.where_label),
            # Esperamos hasta que el elemento 'signin_button' esté presente en la página
            GeneralComponents.wait_until_element_is_present(self.driver, HomeWebElements.signin_button))

    # Método para obtener el título de la página actual
    def get_title_page(self):
        return self.driver.title
