create database concurso_preguntas;
use concurso_preguntas;

create table categorias(
	Id int primary key,
    nombre varchar(50),
    dificultad int
);

create table jugadores(
    nickName nvarchar(100) primary key,
    nombre varchar(50),
    puntaje int
);

create table juegos(
	Id int auto_increment primary key,
    nickNameJugador nvarchar(100),
    rondaMaxima int,
    puntajeMaximo int,
    acumulado int,
    finalForzado boolean
);


create table preguntas(
	Id int primary key,
    id_categoria int,
    enunciado nvarchar(300),
    opcion1 nvarchar(100),
    opcion2 nvarchar(100),
    opcion3 nvarchar(100),
    opcion4 nvarchar(100),
    correcta int
);

alter table preguntas add foreign key(id_categoria) references categorias(Id);
alter table juegos add foreign key(nickNameJugador) references jugadores(nickName);

insert into categorias (Id, nombre, dificultad) values (1, "deportes", 1),(2, "historia", 2),(3, "arte", 3),(4, "geografia", 4),(5, "ciencia", 5);
insert into preguntas (Id, id_categoria, enunciado, opcion1, opcion2, opcion3, opcion4, correcta) values
(1, 1, "¿Cuántos jugadores por equipo participan en un partido de voleibol?", "6","2","4","5", 1),
(2, 1, "¿Cuál es la altura de la red de voleibol en los juegos masculino y femenino?", "2,5 m y 2,0 m", "2,43 m y 2,24 m", "1,8 m y 1,5 m", "2,4 m para ambos", 2),
(3, 1, "¿Cuántos jugadores pueden participar por equipo en el basquetbol?", "2","3","5","4",3),
(4, 1, "¿Cuántos jugadores pueden participar por equipo en el futbol?", "10","12","9","11",4),
(5, 1, "¿Que deporte practica Cristiano Ronaldo?", "futbol","basquetbol","voleibol","ciclismo", 1),

(6,2, "¿En qué periodo de la prehistoria fue descubierto el fuego?", "Neolítico","Paleolítico","Edad de los metales","Edad de piedra",2),
(7,2, "¿Qué líder mundial quedó conocida como 'La Dama de Hierro'?", "Margaret Thatcher", "Hillary Clinton", "Angela Merkel", "Dilma Rouseff", 1),
(8,2, "¿Qué es el Acuerdo de París?", "El acuerdo entre países europeos acerca de la inmigración.","El acuerdo entre Francia, EE.UU y Canadá para acusar a China del calentamiento global.","El acuerdo de cooperación financiera internacional entre las tres mayores potencias mundiales.","El acuerdo entre varios países acerca de las consecuencias del calentamiento global.",4),
(9,2, "¿Qué es la Triple Alianza?", "El acuerdo económico entre México, EE.UU y Canadá.","El anillo que se intercambian los novios cuando contraen matrimonio.","El acuerdo entre Alemania, el imperio Austro-Húngaro e Italia para apoyarse en caso de guerra.","El acuerdo económico entre Inglaterra, Francia y Rusia.",3),
(10,2, "¿Cuál es la religión monoteísta que cuenta con el mayor número de adeptos en el mundo?", "Cristianismo","Zoroastrismo","Judaísmo","Hinduismo",1),

(11,3, "¿Quién pintó la obra 'Guernica'?", "Pablo Picasso","Salvador Dalí","Frida Kahlo","Paul Cézanne", 1),
(12,3, "¿Por qué película recibió un premio Oscar Leonardo DiCaprio?", "The Revenant (2015)","Diamantes de sangre (2006)","Titanic (1997)","El Lobo de Wall Street (2013)",1),
(13,3, "¿Cuál de estas películas se basó en el plebiscito chileno de 1988?", "NO","Diarios de motocicleta","Pinochet in Suburbia","Enterrados vivos",1),
(14,3, "¿Cuál artista es conocido como uno de los exponentes máximos del ready-made (objeto-encontrado)?", "Marcel Duchamp","Van Gogh","Leonardo de Vinci","Salvador Dalí",1),
(15,3, "¿Quién pintó la bóveda de la capilla sixtina?", "Miguel Angel","Boticelli","Donatello","Leonardo da Vinci",1),

(16,4, "¿Cuál es el país más grande y el más pequeño del mundo?", "Canadá y Mónaco","Rusia y Vaticano","China y Nauru","India y San Marino",2),
(17,4, "¿Cuál es la montaña más alta del continente americano?", "Pico Neblina","Aconcagua","Pico Bolívar","Monte Everest",2),
(18,4, "¿En qué país de África el español es la lengua oficial?", "Cabo Verde","Guinea ecuatorial","Liberia","Costa de Marfil",2),
(19,4, "¿Cuáles de estas construcciones famosas quedan en los Estados Unidos?", "Dancing House, 30 st Mary Axe, La Casa Blanca","Estatua de la Libertad, puente Golden Gate, Empire State Building","La ciudad prohibida, la Sagrada Familia, el Panteón","Lincoln Memorial, Sydney Opera House, Burj Khalifa",2),
(20,4, "¿Cuál de estos países se extiende entre dos continentes?", "Tanzania","Rusia","Groenlandia","Egipto",2),

(21,5, "¿Cuántos litros de sangre tiene una persona adulta?", "Tiene entre 2 y 4 litros","Tiene entre 4 y 6 litros","Tiene 10 litros","Tiene 7 litros", 2),
(22,5, "¿Cuál es el cromosoma que determina el sexo masculino?", "El cromosoma Y","El cromosoma X","El cromosoma Z","El cromosoma M",1),
(23,5, "¿Cuál es el metal cuyo símbolo químico es Au?", "Arsénico","Antimonio","Actinio","Oro",4),
(24,5, "¿Dónde se encuentra el gran colisionador de hadrones?", "Entre Francia y Suiza","Entre Italia y Alemania","Entre EE.UU y Canadá","Entre Portugal y España",1),
(25,5, "¿Cuáles de los siguientes compuestos son polisacáridos?", "Almidón y celulosa","Glucosa y fructosa","Metano y etano","Insulina y vitamina A",1);