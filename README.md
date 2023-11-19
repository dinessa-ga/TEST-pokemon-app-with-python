<h1> Proyecto de Pokemon con python Django </h1>

La página web muestra una lista de pokemones, y luego al darle clic a cada tarjeta, la siguiente interfaz muestra más información sobre cada pokemon.

Este proyecto utiliza Django un framework para Python, y se alimenta de una api externa, PokeApi. Además contiene una carpeta, PokemonApp, dentro en la carpeta templates, contiene la carpeta main, donde se encuentran los html: 

- **index.html** - Contiene la vista principal que contiene la lista de pokemones
- **details.html** - Contiene la vista de cada pokemon

La carpeta PokemonApp se compone de los siguientes archivos python principales: 
- **urls.py:** Se realiza el ruteo de las vistas 
- **views.py:** Está la funcionalidad de cada vista
- **api.py:** Se realiza el consumo de la api de pokemon

Fuera de PokemonApp se incluye la carpeta, static, dentro está el CSS e IMG. 

<h3>Para desplegar este proyecto solo debes descargarlo a tu computadora y deberás tener los siguientes requerimientos, dejo las indicaciones para windows.</h3>

- Tener Python 3.11.2

- Dependencias pip actualizadas: python -m pip install --upgrade pip
- Debes tomar en cuenta que para poder instalar el framework Django y desplegar, debes crear y habilitar un entorno virtual: **python -m venv myvenv** - este es un ejemplo "myvenv" es el nombre que darás al entorno.

- Instalación: pip install django

- Instalación de las dependencias de requests: pip install requests

- Desplegar: python manage.py runserver 





