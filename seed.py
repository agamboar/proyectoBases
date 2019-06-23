import psycopg2 as psq
from datosMaster import *

conexion = psq.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,password))

cur = conexion.cursor()

sql = '''
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, despedido)
              VALUES('12025231-8', 'Esteban', 'Gomez', 'Torres', FALSE);
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, despedido)
              VALUES('9784124-K', 'Raul', 'Flores', 'Martinez', FALSE);
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, despedido)
              VALUES('10111222-4', 'Mario', 'Lopez', 'Torres', FALSE);
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, despedido)
              VALUES('7845111-4', 'Manuel', 'Lara', 'Donoso', FALSE);
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, despedido)
              VALUES('11324587-0', 'Mario', 'Castro', 'Urzua', FALSE);  
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, despedido)
              VALUES('6879123-4', 'Hernan', 'Florez', 'Donoso', TRUE);
              
    INSERT INTO camion(patente, capacidad, fecha_ult_mantencion, empresa)
              VALUES('TR1012', 2000, '2019-03-03', 'APL');
    INSERT INTO camion(patente, capacidad, fecha_ult_mantencion, empresa)
              VALUES('ZA1144', 2400, '2018-12-15', 'TTT');
    INSERT INTO camion(patente, capacidad, fecha_ult_mantencion, empresa)
              VALUES('UA6799', 1500, '2019-05-20', 'APL');                    
    INSERT INTO camion(patente, capacidad, fecha_ult_mantencion, empresa)
              VALUES('DFPK12', 4000, '2019-04-09', 'TTT');          
              
    
              
              
              
              
              
              
              
              
                                  
'''