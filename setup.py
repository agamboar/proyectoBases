import psycopg2 as psq
from datosMaster import *

conn = psq.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,password))

cur = conn.cursor()

sql = """select 'drop table"' || tablename || '" cascade;' from pg_tables;"""

cur.execute(sql)

sql = """

CREATE TABLE chofer
        (rut VARCHAR(10) PRIMARY KEY NOT NULL, nombre VARCHAR(15), apellidoP VARCHAR(15), apellidoM VARCHAR(15), sueldo INT, despedido BOOLEAN);
          
CREATE TABLE camion
        (patente VARCHAR(6) PRIMARY KEY NOT NULL, capacidad INTEGER, fecha_ult_mantencion DATE, empresa VARCHAR (20));

CREATE TABLE destino
        (cod_destino INT PRIMARY KEY NOT NULL, ciudad VARCHAR(25), num_bodegas INT);

CREATE TABLE bodegas
        (cod_bodega INT PRIMARY KEY NOT NULL, direccion VARCHAR(30), capacidad INT);

CREATE TABLE productos
        (cod_producto INT PRIMARY KEY NOT NULL, marca VARCHAR(15), tipo VARCHAR(15));

CREATE TABLE envios
        (cod_envio INT PRIMARY KEY NOT NULL, fecha_pedido DATE, fecha_limite DATE);
        
CREATE TABLE detalle_envios
        (cod_envio INT, cod_producto INT, FOREIGN KEY(cod_envio) REFERENCES envios(cod_envio), FOREIGN KEY(cod_producto) REFERENCES productos(cod_producto), PRIMARY KEY(cod_envio, cod_producto), cantidad INT);
                        
/*TABLA RELACIONAL DE ENVIOS CON CAMION  #n:m */
CREATE TABLE envio_camion
        (cod_envio INT, patente VARCHAR(6), FOREIGN KEY(cod_envio) REFERENCES envios(cod_envio), FOREIGN KEY(patente) REFERENCES camion(patente));
      
/*TABLA RELACIONAL DE ENVIOS CON CHOFER #n:m */
CREATE TABLE envio_chofer
        (cod_envio INT, rut VARCHAR(10), FOREIGN KEY(cod_envio) REFERENCES envios(cod_envio), FOREIGN KEY(rut) REFERENCES chofer(rut));

/*TABLA RELACIONAL DE ENVIOS CON DESTINO #n:1 */
CREATE TABLE envio_destino
        (cod_envio INT, cod_destino INT, FOREIGN KEY(cod_envio) REFERENCES envios(cod_envio), FOREIGN KEY(cod_destino) REFERENCES destino(cod_destino));        

CREATE TABLE despedidos
        (id_despido INT, rut VARCHAR(15), FOREIGN KEY(rut) REFERENCES chofer(rut), PRIMARY KEY(id_despido, rut), fecha_despido DATE);      

/*TABLA RELACIONAL DE CHOFER CON CAMION #n:m*/      
CREATE TABLE chofer_camion
        (rut VARCHAR (10), patente VARCHAR(6), FOREIGN KEY(rut) REFERENCES chofer(rut), FOREIGN KEY(patente) REFERENCES camion(patente));

/*TABLA RELACIONAL DE DESTINO CON BODEGAS #1:m  */
CREATE TABLE destino_bodega
        (cod_destino INT, cod_bodega INT, FOREIGN KEY(cod_destino) REFERENCES destino(cod_destino), FOREIGN KEY(cod_bodega) REFERENCES bodegas(cod_bodega));
        
"""

cur.execute(sql)

conn.commit()

cur.close()

conn.close()

