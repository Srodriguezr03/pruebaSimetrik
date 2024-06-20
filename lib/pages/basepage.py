
# Importamos
from selenium.common.exceptions import NoSuchElementException

from lib.helpers.generalhelpers import transformation_to_element_name


# Definimos la clase BasePage, que actúa como la clase base para todas las páginas en la aplicación
class BasePage(object):
    def __init__(self, driver, context):
        # Inicializamos el driver y la URL base de la página dependiendo del entorno
        self.driver = driver
        self.base_url = self.get_url_per_environment(context)

    # Método para eliminar todas las cookies
    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    # Método para recargar la página actual
    def reload_page(self):
        self.driver.refresh()

    # Método para visitar una página específica
    def visit_page(self, url):
        self.driver.get(url)

    # Método para cerrar la ventana del navegador actual
    def close(self):
        self.driver.close()

    # Método para cerrar completamente el navegador
    def quit(self):
        self.driver.quit()

    # Método para obtener la URL actual de la página
    def get_current_url(self):
        return self.driver.current_url

    # Método para encontrar múltiples elementos en la página
    def find_elements(self, selector):
        try:
            return self.driver.find_elements(selector[0], selector[1])
        except NoSuchElementException as e:
            raise e

    # Método para cambiar a una ventana específica
    def switch_to(self, window_name):
        return self.driver.switch_to.window(window_name)

    # Método para obtener el manejador de la ventana actual
    def current_window_handle(self):
        return self.driver.current_window_handle

    # Método para visitar una URL, si la URL es vacía se usa la URL base
    def visit(self, url):
        if url == "":
            return self.driver.get(self.base_url)
        else:
            return self.driver.get(url)

    # Método para obtener los manejadores de ventana por posición
    def get_window_handles_per_position(self, position):
        return self.driver.window_handles[position]

    # Método estático para obtener la URL base dependiendo del entorno
    @staticmethod
    def get_url_per_environment(context):
        country = context.config.userdata["country"]
        return '{}{}'.format("https://www.kayak.com.", country)

    # Método para obtener el título de la página actual
    def get_title_page(self):
        return self.driver.title

    # Método para verificar si los elementos están presentes en la página
    def are_element_presents(self, list_element, context):
        validation_list = []
        elements = transformation_to_element_name(list_element)
        for element in elements:
            selector = getattr(context.current_page.webElements, element, None)
            if selector is None:
                raise TypeError(f'The selector name for {element} is not created in webElements')
            web_element = self.find_elements(selector)
            validation_list.append(len(web_element) > 0)
        return validation_list
