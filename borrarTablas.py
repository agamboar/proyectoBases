import psycopg2 as psq
from datosMaster import *

conexion = psq.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,password))

cur = conexion.cursor()

sql = """select 'drop table"' || tablename || '" cascade;' from pg_tables;"""

cur.execute(sql)


sql= '''
DROP TABLE usuario CASCADE ;
DROP TABLE despedidos CASCADE ;
/*DROP TABLE chofer_despidos;*/
DROP TABLE chofer CASCADE;
DROP TABLE chofer_camion CASCADE ;
DROP TABLE camion CASCADE ;
DROP TABLE destino CASCADE ;
DROP TABLE destino_bodega CASCADE ;
DROP TABLE bodegas CASCADE ;
DROP TABLE productos CASCADE ;
/*DROP TABLE producto_detalle;*/
DROP TABLE detalle_envios CASCADE ;
DROP TABLE envios CASCADE ;
DROP TABLE envio_camion CASCADE ;
/*DROP TABLE envio_detalle;*/
DROP TABLE envio_chofer CASCADE ;
DROP TABLE envio_destino CASCADE ;

'''

cur.execute(sql)

conexion.commit()

cur.close()

conexion.close()