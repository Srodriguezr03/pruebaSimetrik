from selenium.webdriver.common.by import By

class HomeWebElements:
    where_label = (By.XPATH, '//*[@id="main-search-form"]/div/div/div[1]/div/div/h2')  # Etiqueta "Donde" en el formulario principal
    signin_button = (By.XPATH, '//*[@id="root"]/div/header/div/div[2]/div/div[3]/div/div/span/div/div')  # Botón de inicio de sesión
    flights_button = (By.XPATH, '//a[@href="/flights"]')  # Botón de vuelos
    stays_button = (By.XPATH, '//a[@href="/stays"]')  # Botón de estancias
    car_button = (By.XPATH, '//a[@href="/cars"]')  # Botón de alquiler de coches
    flight_hotel_button = (By.XPATH, '//a[@href="/citybreaks"]')  # Botón de paquetes de vuelo y hotel
    explore_button = (By.XPATH, '//a[@aria-label="Ir a Explore "]')  # Botón de explorar
    blog_button = (By.XPATH, '//a[@aria-label="Visita nuestro blog "]')  # Botón de blog
