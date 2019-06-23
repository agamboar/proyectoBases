import psycopg2 as psq
from datosMaster import *

conexion = psq.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,password))

cur = conexion.cursor()

sql = """select 'drop table"' || tablename || '" cascade;' from pg_tables;"""

cur.execute(sql)


sql= '''

DROP TABLE despedidos;
DROP TABLE chofer_despedidos;
DROP TABLE chofer;
DROP TABLE chofer_camion;
DROP TABLE camion;
DROP TABLE destino;
DROP TABLE destino_ciudad;
DROP TABLE bodegas;
DROP TABLE productos;
DROP TABLE producto_detalle;
DROP TABLE detalle_envio;
DROP TABLE envios;
DROP TABLE envio_camion;
DROP TABLE envio_detalle;
DROP TABLE envio_chofer;
DROP TABLE envio_destino;

'''

cur.execute(sql)

conexion.commit()

cur.close()

conexion.close()