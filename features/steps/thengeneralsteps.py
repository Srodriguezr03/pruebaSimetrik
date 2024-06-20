# Importamos
from behave import then, use_step_matcher
from hamcrest import equal_to, assert_that, only_contains
from lib.components.generalcomponents import GeneralComponents
from lib.helpers.generalhelpers import validate_text, transform_validation

# Configuramos el uso de un step matcher de expresiones regulares para coincidir con los patrones de pasos
use_step_matcher("re")

# Definimos un paso 'then' para validar el título de la página
@then(u'The page title should "(?P<assertion>contain|equal)" the "(?P<page_name>.*)" text')
def step_impl(context, assertion, page_name):
    # Validamos el texto del título de la página
    validation_result = validate_text(assertion, page_name, context.current_page.get_title_page())
    # Realizamos una aserción con Hamcrest
    assert_that(validation_result, equal_to(True),
                f'The expected title to {"contain" if assertion == "contain" else "be equal to"} "{page_name}", but was "{context.current_page.get_title_page()}"')

# Definimos un paso 'then' para verificar que estamos en la página correcta
@then(u'I should be in the "(?P<page>.*)" page')
def step_impl(context, page):
    # Configuramos la página actual en el contexto
    context.current_page = context.all_contexts[page]
    # Realizamos una aserción para verificar que la página está abierta
    assert_that(context.current_page.is_open(), only_contains(True),
                f'Some element is not present in the opened "{page}" page')

# Definimos un paso 'then' para verificar que la página contiene ciertos elementos
@then(u'The page "(?P<expression>should|should not)" contain the next elements')
def step_impl(context, expression):
    # Validamos que los elementos están presentes en la página
    list_validation = context.browser.are_element_presents(context.table, context)
    # Transformamos la expresión para la aserción
    assertion = transform_validation(expression)
    # Realizamos una aserción con Hamcrest
    assert_that(list_validation, only_contains(assertion))

# Definimos un paso 'then' para verificar que la URL actual es la esperada
@then(u'The url page should be equal to the next "(?P<url>.*)" url')
def step_impl(context, url):
    # Esperamos hasta que la URL sea la esperada
    GeneralComponents.wait_until_url_is(context.browser, url)
    # Obtenemos la URL actual del navegador
    current_url = context.browser.get_current_url()
    # Realizamos una aserción con Hamcrest
    assert_that(current_url, equal_to(url),
                f'Expected URL to be "{url}" but found "{current_url}"')
