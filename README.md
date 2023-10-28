# ReadConnect Backend
¡Hola! Este es el backend del proyecto ReadConnect. Esta desarrollado en django y sirve una api GraphQl. La base de datos esta alojada en Amazon y fue creada con los modelos de Django.

## Pasos realizados

- Creé el modelo de la aplicación en base al archivo entregado. Los usuarios tienen listas de libros por leer y libros leidos. Los libros tienen categorias y autores. Las críticas son entre libros y usuarios. El modelo se encuentra [aquí](https://github.com/stixbunny/readconnect_back/blob/main/website/models.py).
- Para crear la base de datos con los datos, establecí una instancia en RDS y los datos se llenaron por medio de fixtures de Django. Para esto [edité](https://github.com/stixbunny/readconnect_back/blob/main/fix_json.py) el json original y luego [prepare](https://github.com/stixbunny/readconnect_back/blob/main/create_fixture.py) los [fixtures](https://github.com/stixbunny/readconnect_back/blob/main/fixture.json) correspondientes, tomando en cuenta autores y categorias unicas.
- Finalmente se utilizó la librería [graphene-django](https://github.com/graphql-python/graphene-django) para exponer [la](https://github.com/stixbunny/readconnect_back/blob/main/website/types.py) [api](https://github.com/stixbunny/readconnect_back/blob/main/website/schema.py) como GraphQl con especificación de Relay

## Lo que no quedó

Por temas de tiempo y utilización de librerias y tecnologías nuevas (es la primera vez que utilizao GraphQl) mucho del proyecto esta inconcluso, incluyendo queries de autores y categorias (por temas de optimizacion de consulta) y autentificacion de usuarios.
Otro punto importante es como esta almacenado en Amazon EC2 no alcancé a configurar un certificado SSL para que se pudiera consumir desde la aplicación en Amazon Amplify (que esta en https), por lo que no funciona como debe.

## Finalmente

La dirección de las consultas esta en http://3.142.82.177/graphql la cual se puede analizar con introspeccion y hacer queries por algun servicio como postman.
