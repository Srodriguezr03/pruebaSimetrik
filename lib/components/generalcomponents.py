import datetime
import logging
import time
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from lib.constants import Constants
from lib.helpers.generalhelpers import transformation_to_element_name

logger = logging.getLogger(__name__)


class GeneralComponents:
    @staticmethod
    def wait_until_element_is_present(driver, web_element, timeout=10):
        """
        Espera hasta que el elemento esté presente en el DOM.
        """
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(web_element))

    @staticmethod
    def wait_until_element_is_clickable(driver, web_element, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que el elemento sea clicable en el DOM.
        """
        error_message = f'The "{web_element}" element took more than {timeout} seconds to be clickable in the DOM.'
        try:
            return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(web_element), error_message)
        except TimeoutException as e:
            raise e

    def wait_until_element_is_not_present(self, web_element, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que el elemento no esté presente en el DOM.
        """
        error_message = f'The "{web_element}" element took more than {timeout} seconds to disappear from the DOM.'
        try:
            element_present = EC.invisibility_of_element(web_element)
            return WebDriverWait(self.web_driver, timeout).until(element_present, error_message)
        except TimeoutException as e:
            raise e

    def wait_until_title_is(self, title, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que el título de la página sea igual al especificado.
        """
        error_message = f'The title page is not equal to the "{title}" title after {timeout} seconds.'
        try:
            return WebDriverWait(self.web_driver, timeout).until(EC.title_is(title), error_message)
        except TimeoutException as e:
            raise e

    def wait_until_title_contain(self, title, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que el título de la página contenga el texto especificado.
        """
        error_message = f'The title page does not contain the "{title}" title after {timeout} seconds.'
        try:
            return WebDriverWait(self.web_driver, timeout).until(EC.title_contains(title), error_message)
        except TimeoutException as e:
            raise e

    def wait_until_text_is_present_in_value(self, locator, text, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que el texto esté presente en el valor del elemento.
        """
        error_message = f'Text in value is not present after {timeout} seconds.'
        try:
            return WebDriverWait(self.web_driver, timeout).until(EC.text_to_be_present_in_element_value(locator, text), error_message)
        except TimeoutException as e:
            raise e

    def wait_until_element_is_not_visible(self, web_element, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que el elemento no sea visible en el DOM.
        """
        error_message = f'The "{web_element}" element took more than {timeout} seconds to disappear from the DOM.'
        try:
            return WebDriverWait(self.web_driver, timeout, 1).until(EC.invisibility_of_element(web_element), error_message)
        except TimeoutException as e:
            raise e

    def wait_until_element_is_visible(self, web_element, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que el elemento sea visible en el DOM.
        """
        error_message = f'The "{web_element}" element took more than {timeout} seconds to become visible in the DOM.'
        try:
            return WebDriverWait(self.web_driver, timeout, 1).until(EC.visibility_of(web_element), error_message)
        except TimeoutException as e:
            raise e

    def wait_until_two_elements_are_present(self, web_element_1, web_element_2, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que dos elementos estén presentes en el DOM.
        """
        error_message = f'The elements took more than {timeout} seconds to be present in the DOM.'
        try:
            return WebDriverWait(self.web_driver, timeout).until(
                EC.all_of(EC.presence_of_element_located(web_element_1), EC.presence_of_element_located(web_element_2)), error_message)
        except TimeoutException as e:
            raise e

    def wait_until_two_elements_are_clickable(self, web_element_1, web_element_2, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que dos elementos sean clicables en el DOM.
        """
        error_message = f'The elements took more than {timeout} seconds to be clickable in the DOM.'
        try:
            return WebDriverWait(self.web_driver, timeout).until(
                EC.all_of(EC.element_to_be_clickable(web_element_1), EC.visibility_of_element_located(web_element_2)), error_message)
        except TimeoutException as e:
            raise e

    @staticmethod
    def wait_until_url_is(driver, url, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que la URL actual sea igual a la especificada.
        """
        error_message = f'The page does not contain the {url} url after {timeout} seconds.'
        try:
            return WebDriverWait(driver, timeout).until(lambda driver: driver.get_current_url() == url, error_message)
        except TimeoutException as e:
            raise TimeoutException(error_message) from e

    @staticmethod
    def find_into_element(web_element, selector) -> WebElement:
        """
        Encuentra un elemento dentro de otro elemento usando un selector.
        """
        try:
            return web_element.find_element(selector[0], selector[1])
        except NoSuchElementException as e:
            raise e

    @staticmethod
    def find_elements_into_element(web_element, selector):
        """
        Encuentra múltiples elementos dentro de otro elemento usando un selector.
        """
        try:
            return web_element.find_elements(selector[0], selector[1])
        except NoSuchElementException as e:
            raise e

    @staticmethod
    def is_element_present_in_component(list_element, context, component_name):
        """
        Verifica si los elementos están presentes en un componente.
        """
        validation_list = []
        elements = transformation_to_element_name(list_element)
        for element in elements:
            component_elements = context.current_page.get_component_elements_per_name(component_name)
            web_element = context.browser.find_elements(component_elements.__dict__.get(element))
            validation_list.append(len(web_element) > 0)
        return validation_list

    @staticmethod
    def get_text_element_in_value_attribute(context, selector_name) -> str:
        """
        Obtiene el texto del atributo 'value' de un elemento.
        """
        element = context.current_page.webElements.__dict__.get(selector_name)
        return context.browser.find_element(element).get_attribute("value")

    @staticmethod
    def get_attribute_of_element(element, attribute):
        """
        Obtiene el valor de un atributo de un elemento.
        """
        return element.get_attribute(attribute)

    @staticmethod
    def get_text_element(context, selector_name) -> str:
        """
        Obtiene el texto de un elemento.
        """
        element = context.current_page.webElements.__dict__.get(selector_name)
        return context.browser.find_element(element).text

    @staticmethod
    def get_text_web_element(web_element):
        """
        Obtiene el texto de un WebElement.
        """
        return web_element.text

    @staticmethod
    def check_exist_element(context, selector_name):
        """
        Verifica si un elemento existe en la página actual.
        """
        try:
            element = context.current_page.webElements.__dict__.get(selector_name)
            context.browser.find_element(element)
        except NoSuchElementException as e:
            logger.error(e)
            return False
        return True

    @staticmethod
    def check_unique_elements(element_list):
        """
        Verifica si los elementos en una lista son únicos.
        """
        return len(set(element_list)) == len(element_list)

    @staticmethod
    def check_search_elements(element_list, value):
        """
        Verifica si todos los elementos de una lista contienen un valor específico.
        """
        element_list = element_list[1:-1]
        return all(value in item for item in element_list)

    @staticmethod
    def click_multiple_items(element_list):
        """
        Hace clic en múltiples elementos en una lista.
        """
        clicked_items = []
        for elements in element_list:
            clicked_items.append(elements.click())
        return clicked_items

    @staticmethod
    def string_to_list(value, separator=str):
        """
        Convierte una cadena a una lista usando un separador.
        """
        return value.split(separator)

    @staticmethod
    def click_component_by_name(context, component_name, name_element):
        """
        Hace clic en un componente por nombre.
        """
        component_elements = context.current_page.get_component_elements_per_name(component_name)
        web_element = context.browser.find_element(component_elements.__dict__.get(name_element))
        return web_element.click()

    @staticmethod
    def list_to_string(value, separator=str):
        """
        Convierte una lista a una cadena usando un separador.
        """
        return separator.join(map(str, value))

    @staticmethod
    def current_date():
        """
        Obtiene la fecha y hora actual en formato de cadena.
        """
        today = datetime.today()
        return str(today).replace(":", "_").replace(".", "_").replace("-", "_")

    @staticmethod
    def is_enabled_in_component(context, component_name, element_name) -> bool:
        """
        Verifica si un elemento está habilitado en un componente.
        """
        component_elements = context.current_page.get_component_elements_per_name(component_name)
        web_element = context.browser.find_element(component_elements.__dict__.get(element_name))
        return web_element.is_enabled()

    @staticmethod
    def clear_textbox(web_element):
        """
        Limpia el texto de un cuadro de texto.
        """
        return web_element.clear()

    @staticmethod
    def type_in_textbox(txt, web_element):
        """
        Escribe texto en un cuadro de texto.
        """
        GeneralComponents.clear_textbox(web_element)
        return web_element.send_keys(txt)

    @staticmethod
    def get_text_element_from_component(context, component_name, element_name) -> str:
        """
        Obtiene el texto de un elemento en un componente.
        """
        component_elements = context.current_page.get_component_elements_per_name(component_name)
        web_element = context.browser.find_element(component_elements.__dict__.get(element_name))
        return web_element.text

    def wait_until_element_searched_is_present(self, web_element, expected_text, timeout=Constants.MEDIUM_WAIT):
        """
        Espera hasta que el texto esperado esté presente en un elemento.
        """
        error_message = f'The element took more than {timeout} seconds to be present in the DOM.'
        try:
            return WebDriverWait(self.web_driver, timeout).until(EC.text_to_be_present_in_element(web_element, expected_text), error_message)
        except TimeoutException as e:
            raise e

    @staticmethod
    def is_enabled_in_page(context, element_name) -> bool:
        """
        Verifica si un elemento está habilitado en la página actual.
        """
        web_element = context.current_page.webElements.__dict__.get(element_name)
        return context.browser.find_element(web_element).is_enabled()

    @staticmethod
    def get_element_list_from_component(context, component_name, element_name):
        """
        Obtiene una lista de elementos habilitados en un componente.
        """
        enabled_elements = []
        component_elements = context.current_page.get_component_elements_per_name(component_name)
        element_list = context.browser.find_elements(component_elements.__dict__.get(element_name))
        for element in element_list:
            if GeneralComponents.is_enabled_in_component(context, component_name, element_name):
                enabled_elements.append(element)
        return enabled_elements

    @staticmethod
    def type_in_textarea(context, component_name, element_name, text):
        """
        Escribe texto en un área de texto dentro de un componente.
        """
        component_elements = context.current_page.get_component_elements_per_name(component_name)
        web_element = context.browser.find_element(component_elements.__dict__.get(element_name))
        web_element.clear()
        return web_element.send_keys(text)

    @staticmethod
    def check_format_matches(test_format, expected_format):
        """
        Verifica si un formato de fecha y hora coincide con el formato esperado.
        """
        try:
            test_format = datetime.strptime(test_format, expected_format)
            return bool(datetime.strftime(test_format, expected_format))
        except ValueError:
            return False

    @staticmethod
    def is_clickable(context, component_name, element_name) -> bool:
        """
        Verifica si un elemento es clicable en un componente.
        """
        component_elements = context.current_page.get_component_elements_per_name(component_name)
        web_element = context.browser.find_element(component_elements.__dict__.get(element_name))
        return web_element.isClickable()

    @staticmethod
    def is_displayed(context, component_name, element_name):
        """
        Verifica si un elemento está visible en un componente.
        """
        component_elements = context.current_page.get_component_elements_per_name(component_name)
        web_element = context.browser.find_element(component_elements.__dict__.get(element_name))
        return web_element.is_displayed()
