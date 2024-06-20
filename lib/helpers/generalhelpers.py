from selenium.webdriver.remote.webelement import WebElement

def validate_text(comparison_type, text_a, text_b):
    """
    Valida si el texto `text_a` está contenido en `text_b` o si son iguales según `comparison_type`.

    Args:
        comparison_type (str): Tipo de comparación ('contain' para contener, cualquier otro valor para igualdad).
        text_a (str): Texto a comparar.
        text_b (str): Texto con el cual comparar.

    Returns:
        bool: True si la comparación es exitosa, False si no.
    """
    if comparison_type == 'contain':
        return text_a.strip() in text_b.strip()
    else:
        return text_a.strip() == text_b.strip()

def transformation_helper(name, element_type):
    """
    Transforma `name` y `element_type` en un formato específico para identificar elementos.

    Args:
        name (str): Nombre del elemento.
        element_type (str): Tipo de elemento (button, dropdown, option).

    Returns:
        str: Nombre transformado del elemento.
    """
    return '{}{}{}'.format(name.lower(), "_", element_type.lower())

def transformation_to_element_name(list_element):
    """
    Transforma una lista de elementos en un formato específico para identificar nombres de elementos.

    Args:
        list_element (list): Lista de elementos con estructura {'name': nombre, 'type': tipo}.

    Returns:
        list: Lista de nombres transformados de elementos.
    """
    elements = []
    for element in list_element:
        name = f"{element['name']}_{element['type']}"
        elements.append(name)
    return elements

def transform_validation(expression):
    """
    Transforma una expresión de validación en un valor booleano.

    Args:
        expression (str): Expresión de validación ('should' o cualquier otra cosa).

    Returns:
        bool: True si la expresión es 'should', False si no.
    """
    final_expression = True
    if expression != "should":
        final_expression = False
    return final_expression

def validate_wait_results(*waits):
    """
    Valida los resultados de las esperas.

    Args:
        *waits: Lista de objetos o resultados de espera.

    Returns:
        list: Lista de resultados de validación (True o False).
    """
    validation_results = []
    for wait in waits:
        if isinstance(wait, WebElement):
            validation_results.append(True)
        else:
            validation_results.append(wait)
    return validation_results

def clean_behave_list(behave_list):
    """
    Limpia una lista de listas Behave para obtener una lista plana.

    Args:
        behave_list (list): Lista de listas Behave.

    Returns:
        list: Lista plana de elementos.
    """
    cleaned_list = []
    for row in behave_list:
        cleaned_list.append(row[0])
    return cleaned_list

def split_and_replace_string(text_element) -> list:
    """
    Divide un string por espacios y reemplaza saltos de línea por espacios en blanco.

    Args:
        text_element (str): Texto a procesar.

    Returns:
        list: Lista de palabras resultante.
    """
    new_string = []
    for x in text_element.split(" "):
        new_string.append(x.replace("\n", ""))
    return new_string

def join_words(word_list) -> str:
    """
    Une una lista de palabras en un solo string.

    Args:
        word_list (list): Lista de palabras.

    Returns:
        str: String resultante de la unión de palabras.
    """
    new_str = ""
    for word in word_list:
        new_str += word
    return new_str
