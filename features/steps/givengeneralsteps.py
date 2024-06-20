# Importamos las funciones necesarias de Behave
from behave import given, use_step_matcher

# Configuramos el uso de un step matcher de expresiones regulares para coincidir con los patrones de pasos
use_step_matcher("re")

# Definimos un paso 'given' que navega a la página principal de Kayak
@given(u'I navigate to the kayak main page')
def visit_login(context):
    # Utilizamos el navegador del contexto para visitar la URL base (presumiblemente definida en la configuración)
    context.browser.visit("")