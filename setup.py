import psycopg2 as psq
from datosMaster import *

conexion = psq.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,password))

cur = conexion.cursor()

sql = """select 'drop table"' || tablename || '" cascade;' from pg_tables;"""

cur.execute(sql)
#AÑADIR A CHOFER EL ATRIBUTO ESTADO (BOOLEANO) QUE INDICA SI ESTA DESPEDIDO O NO
#CREAR TABLA CON DESPEDIDOS, CON EL RUT DE LOS CHOFERES DESPEDIDOS
#ENTIDADES
sql = """

CREATE TABLE despedidos
        (rut VARCHAR(15), id_despido INT, PRIMARY KEY(rut, id_despido), fecha_despido DATE);      

/*TABLA RELACIONAL DE DESPEDIDOS CON CHOFER*/
CREATE TABLE chofer_despidos
        (rut VARCHAR(15));

CREATE TABLE chofer
        (rut VARCHAR(15) PRIMARY KEY NOT NULL, nombre VARCHAR(15), apellidoP VARCHAR(15), apellidoM VARCHAR(15), despedido BOOLEAN);

/*TABLA RELACIONAL DE CHOFER CON CAMION */        
CREATE TABLE chofer_camion
        (rut VARCHAR (15), patente VARCHAR(10));
        
CREATE TABLE camion
        (patente VARCHAR(10) PRIMARY KEY NOT NULL, capacidad INTEGER, fecha_ult_mantencion DATE, empresa VARCHAR (20));


CREATE TABLE destino
        (cod_destino INT PRIMARY KEY NOT NULL, ciudad VARCHAR(25), num_bodegas INT);

/*TABLA RELACIONAL DE DESTINO CON BODEGAS*/
CREATE TABLE destino_ciudad
        (cod_destino INT, cod_bodega INT):
        
CREATE TABLE bodegas
        (cod_bodega INT PRIMARY KEY NOT NULL, direccion VARCHAR(30), capacidad INT);

CREATE TABLE productos
        (cod_producto INT PRIMARY KEY NOT NULL, marca VARCHAR(15), tipo VARCHAR(15));

/*TABLA RELACIONAL DE PRODUCTOS CON DETALLE ENVIOS*/        
CREATE TABLE producto_detalle
        (cod_producto INT);

CREATE TABLE detalle_envios
        (cod_envio INT, cod_producto INT, PRIMARY KEY(cod_envio, cod_producto), cantidad INT);
        
CREATE TABLE envios
        (cod_envio INT PRIMARY KEY NOT NULL, fecha_pedido DATE, fecha_limite DATE);
        
/*TABLA RELACIONAL DE ENVIOS CON CAMION*/
CREATE TABLE envio_camion
        (cod_envio INT, patente VARCHAR(10));

/*TABLA RELACIONAL DE ENVIOS CON DETALLE ENVIOS*/
CREATE TABLE envio_detalle
        (cod_envio INT);        
        
/*TABLA RELACIONAL DE ENVIOS CON CHOFER*/
CREATE TABLE envio_chofer
        (cod_envio INT, rut VARCHAR(15));

/*TABLA RELACIONAL DE ENVIOS CON DESTINO*/
CREATE TABLE envio_destino
        (cod_envio INT, cod_destino INT);        

"""

cur.execute(sql)

conexion.commit()

cur.close()

conexion.close()

