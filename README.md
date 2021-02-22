# Harry Potter API

![HarryPotter](/image/harry_potter.jpg)

Este es un proyecto realizado durante el Bootcamp de Data Anatlytics en [Ironhack](https://www.ironhack.com/es/data-analytics) Madrid.

## Objetivo:

El objetivo de este proyecto es la creación de una API.

He decidido crear una API sobre las peliculas de **Harry Potter**. Para ello me he basado en célebres frases utilizadas en las peliculas de la saga de la escritora británica **J.K. Rowling**.

Harry Potter es una serie de novelas fantásticas en la que se describen las aventuras del joven aprendiz de magia y hechicería Harry Potter y sus amigos Hermione Granger y Ron Weasley, durante los años que pasan en el Colegio Hogwarts de Magia y Hechicería. 

Desde el lanzamiento de la primera novela, [Harry Potter y la piedra filosofal](https://es.wikipedia.org/wiki/Harry_Potter_y_la_piedra_filosofal), en 1997, la serie logró una inmensa popularidad, críticas favorables y éxito comercial alrededor del mundo.

En 1999 la productora de cine **Warner Bros**, adquirió los derechos para adaptar los siete libros a una serie de películas; con ocho películas realizadas la serie se convirtió en una de las franquicias más exitosas del cine en todo el mundo.

## Proceso:

Para conseguir mi objetivo, he seguido los siguientes pasos:

1. Diseñar la estructura de una base de datos:
   * 3 Colecciones:
      - Quotes: 
           - Nombre del personaje ("Characters")
           - Frase célebre ("Phrase")
           - Pelicula en la que aparece ("Movie")
           - Año de la pelicula ("Year")
       - Cast:
           - Nombre del personaje ("Characters")
           - Papel en la pelicula ("Role")
           - Nombre del actor/actriz que lo interpreta ("Actor name")
       - Movies:    
           - Nombre de la pelicula ("Movie")
           - Año del estreno de la pelicula ("Year")
           - Recaudación de la pelicula ("Box office (million $"))
  
* La base de datos utilizada es [MongoDB](https://www.mongodb.com/es).
  
2. Creación de la API; recibir y almacenar datos en la base de datos. La estructura:
   
- *mongoConnection .py*: contiene el código necesario para conectar con la base de datos Mongo y las consultas para llamar y almacenar información.

- *api .py*: conecta la API y proporciona los "Endpoints".

- *checking .py*: _______________________

- *tests.ipynb*: archivo de Jupyter Notebook donde compruebo que la API funciona.

- *data > HP_quotes.csv*: archivo .csv utilzado como ejemplo para la realización de la API.

- *sentiment_analysis*: archivo de Jupyter Notebook donde realizo el "análisis de sentimiento".
   
* La API está creada con [Flask](https://flask.palletsprojects.com/en/1.1.x/).
   
3. Leer y servir datos de la base de datos usando Endpoints.
   
   - Endpoints:
     - /welcome: "Welcome to the magical world of Harry Potter".
     - /phrase: Devuelve todas las frases.
     - /phrase/<phrase>: Devuelve una frase concreta.
     - /characters: Devuelve todos los personajes.
     - /characters/<character>: Devuelve un personaje en concreto.
     - /movies: Devuelve todas las peliculas.
     - /movies/<movie>: Devuelve una peliculas en concreto.
     - /add/new_quote/: Añade una nueva frase.
     - /add/new_char/: Añade un nuevo personaje.
     - /delete_quote/: Elimina una frase.
     - /delete_char/: Elimina un personaje.
   
4. Extraer el valor emocional de las frases. He utilizado las librerias;
   - [TextBlob](https://textblob.readthedocs.io/en/dev/)   
   - [Natural Language Toolkit](https://www.nltk.org/)
  
 - ¿Quieres conocer qué personaje de la muestra realizada tiene la mayor puntuación? 
  
## Referencias:

* [Mongodb](https://www.mongodb.com/3)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [TextBlob](https://textblob.readthedocs.io/en/dev/)   
* [Natural Language Toolkit](https://www.nltk.org/)


## "La felicidad se puede encontrar incluso en los tiempos más oscuros, solo hay que acordarse de encender la luz". - Harry Potter. 
  