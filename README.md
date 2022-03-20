# RetoTecnicoSofka

Saludos! En este repositorio se encuentra la solución al reto técnico del concurso de preguntas. Les daré algunas indicaciones para la facil y completa ejecución del programa.

Primeramente en el repositorio se encuentra la carpeta src en donde está todo el código fuente. Cabe aclarar que el programa está hecho para ser ejecutado por interfaz de consola.
Segundo, en el repo se encuentra el script sql para ser ejecutado para la creación de la base de datos. Como algo adicional a esto, también se encuentra montado aquí el modelado de datos de la base de datos nombrado como concurso_preguntas.png.

### Pasos previos a la ejecución

1. Tener instalado xampp: La base de datos está montada en mysql (editado en el gestor de base de datos MySQL Workbench, utilizar el de su preferencia, puede ser el propio PhpMyAdmin o cualquiera que soporte MySql) y por lo tanto hay que habilitar el puerto para la comunicación con esta base de datos desde este servidor.
2. Crear la base de datos: ejecutar el archivo scriptConcurso.sql adjunto en el repositorio en el gestor de base de datos utilizado.
3. configurar credenciales de la base de datos y servidor: Dentro de la carpeta src, se encuentra el archivo ConexionBD.py, en él debe cambiar la variable 'user' por el usuario que usted tenga configurado en el gestor de base de datos, al igual que 'password' si es que posee una clave, sino es el caso, entonces dejar ese campo en blanco('')
4. Por si existen errores: La versión que yo utilizo de xampp es la 7.4.16 y de Workbench la 8.0.23. La versión de python utilizada es la 3.9.5

### Pasos para la ejecución

1. Tener habilitado el puerto para MySql (por defecto es el 3306)
2. abrir el archivo Interfaz.py dentro de la carpeta src o abrir el proyecto completo dentro de su IDE o editor de código de preferencia y luego ejecutar el archivo Interfaz.py para que empiece a correr por consola.

### Banco de preguntas con sus respectivas respuestas (No mirar para mayor diversión):

#### Categoria de deportes:
1. ¿Cuántos jugadores por equipo participan en un partido de voleibol? R/ 6
2. ¿Cuál es la altura de la red de voleibol en los juegos masculino y femenino? R/ 2,43 m y 2,24 m
3. ¿Cuántos jugadores pueden participar por equipo en el basquetbol? R/ 5
4. ¿Cuántos jugadores pueden participar por equipo en el futbol? R/ 11
5. ¿Que deporte practica Cristiano Ronaldo? R/ futbol

#### Categoria de historia:
1. ¿En qué periodo de la prehistoria fue descubierto el fuego? R/ Paleolítico
2. ¿Qué líder mundial quedó conocida como 'La Dama de Hierro'? R/ Margaret Thatcher
3. ¿Qué es el Acuerdo de París? R/ El acuerdo entre varios países acerca de las consecuencias del calentamiento global.
4. ¿Qué es la Triple Alianza? R/ El acuerdo entre Alemania, el imperio Austro-Húngaro e Italia para apoyarse en caso de guerra.
5. ¿Cuál es la religión monoteísta que cuenta con el mayor número de adeptos en el mundo? R/ Cristianismo

#### Categoria de arte:
1. ¿Quién pintó la obra 'Guernica'? R/ Pablo Picasso
2. ¿Por qué película recibió un premio Oscar Leonardo DiCaprio? R/ The Revenant (2015)
3. ¿Cuál de estas películas se basó en el plebiscito chileno de 1988? R/ NO
4. ¿Cuál artista es conocido como uno de los exponentes máximos del ready-made (objeto-encontrado)? R/ Marcel Duchamp
5. ¿Quién pintó la bóveda de la capilla sixtina? R/ Miguel Angel

#### Categoria de geografia:
1. ¿Cuál es el país más grande y el más pequeño del mundo? R/ Rusia y Vaticano
2. ¿Cuál es la montaña más alta del continente americano? R/ Aconcagua
3. ¿En qué país de África el español es la lengua oficial? R/ Guinea ecuatorial
4. ¿Cuáles de estas construcciones famosas quedan en los Estados Unidos? R/ Estatua de la Libertad, puente Golden Gate, Empire State Building
5. ¿Cuál de estos países se extiende entre dos continentes? R/ Rusia

#### Categoria de ciencia:
1. ¿Cuántos litros de sangre tiene una persona adulta? R/ Tiene entre 4 y 6 litros
2. ¿Cuál es el cromosoma que determina el sexo masculino? R/ El cromosoma Y
3. ¿Cuál es el metal cuyo símbolo químico es Au? R/ Oro
4. ¿Dónde se encuentra el gran colisionador de hadrones? R/ Entre Francia y Suiza
5. ¿Cuáles de los siguientes compuestos son polisacáridos? R/ Almidón y celulosa

# Agradecimientos
Por último, muchas gracias por darme la oportunidad de participar de este proceso, espero que mi solución al reto cumpla con sus expectativas. Quedo muy atento a cualquier duda o inconveniente con la ejecución del programa, me puede contactar al correo santigm1905@gmail.com. Saludos y buena trivia de preguntas!

