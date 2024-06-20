# Importamos
from behave import when, use_step_matcher

from lib.components.generalcomponents import GeneralComponents
from lib.helpers.generalhelpers import transformation_helper

# Configuramos el uso de un step matcher de expresiones regulares para coincidir con los patrones de pasos
use_step_matcher("re")

# Definimos un paso 'when' para hacer clic en un elemento específico
@when(u'I click on the "(?P<element_name>.*)" "(?P<element_type>button|dropdown|option)"')
def step_impl(context, element_name, element_type):
    # Transformamos el nombre del elemento y el tipo para obtener la clave correcta
    element_name = transformation_helper(element_name, element_type)
    # Esperamos hasta que el elemento sea clickeable
    if GeneralComponents.wait_until_element_is_clickable(
            context.driver, context.current_page.webElements.__dict__.get(element_name)
    ):
        # Hacemos clic en el elemento
        context.driver.find_element(*context.current_page.webElements.__dict__.get(element_name)).click()

# Definimos un paso 'when' para navegar a una URL específica
@when(u'I navigate to the "(?P<url>.*)" URL')
def step_impl(context, url):
    # Navegamos a la URL proporcionada
    return context.browser.visit(url)

# Definimos un paso 'when' para seleccionar una opción en un dropdown
@when('I select "(?P<option>.*)" in the dropdown')
def step_impl(context, option):
    # Seleccionamos la opción en el dropdown
    return context.current_page.text_value_in_the_select(option)

# Definimos un paso 'when' para buscar una opción en un input
@when(u'I search "(?P<option>.*)" in the input')
def step_impl(context, option):
    # Ingresamos el texto en el input
    return context.current_page.text_value_in_the_filter(option)
