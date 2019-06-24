import psycopg2 as psq
from datosMaster import *

conexion = psq.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,password))

cur = conexion.cursor()

sql = '''
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, sueldo, despedido)
              VALUES('12025231-8', 'Esteban', 'Gomez', 'Torres', 620000, FALSE);
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, sueldo, despedido)
              VALUES('9784124-K', 'Raul', 'Flores', 'Martinez', 710000, FALSE);
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, sueldo, despedido)
              VALUES('10111222-4', 'Mario', 'Lopez', 'Torres', 650000, FALSE);
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, sueldo, despedido)
              VALUES('7845111-4', 'Manuel', 'Lara', 'Donoso', 750000, FALSE);
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, sueldo, despedido)
              VALUES('11324587-0', 'Mario', 'Castro', 'Urzua', 630000, FALSE);  
    INSERT INTO chofer(rut, nombre, apellidoP, apellidoM, sueldo, despedido)
              VALUES('6879123-4', 'Hernan', 'Florez', 'Donoso', 850000, TRUE);
    /*-----------------------------------------------------------------*/          
    INSERT INTO camion(patente, capacidad, fecha_ult_mantencion, empresa)
              VALUES('TR1012', 2000, '2019-03-03', 'APL');
    INSERT INTO camion(patente, capacidad, fecha_ult_mantencion, empresa)
              VALUES('ZA1144', 2400, '2018-12-15', 'TTT');
    INSERT INTO camion(patente, capacidad, fecha_ult_mantencion, empresa)
              VALUES('UA6799', 1500, '2019-05-20', 'APL');                    
    INSERT INTO camion(patente, capacidad, fecha_ult_mantencion, empresa)
              VALUES('DFPK12', 4000, '2019-04-09', 'EIT');          
    /*---------------------------------------------------------------*/          
    INSERT INTO despedidos( id_despido, rut, fecha_despido)
              VALUES(01 ,'6879123-4', '2019-01-30');
    /*---------------------------------------------------------------
    INSERT INTO chofer_despidos(rut)
              VALUES('6879123-4');
    ---------------------------------------------------------------*/
    INSERT INTO chofer_camion(rut, patente)
              VALUES('12025231-8', 'TR1012');   
    INSERT INTO chofer_camion(rut, patente)
              VALUES('12025231-8', 'UA6799');  
    INSERT INTO chofer_camion(rut, patente)
              VALUES('7845111-4', 'DFPK12');    
    INSERT INTO chofer_camion(rut, patente)
              VALUES('10111222-4', 'DFPK12');
    INSERT INTO chofer_camion(rut, patente)
              VALUES('6879123-4', 'ZA1144');                                   
'''

cur.execute(sql)

sql = '''
    INSERT INTO destino(cod_destino, ciudad, num_bodegas)
              VALUES(001, 'Santiago', 15);
    INSERT INTO destino(cod_destino, ciudad, num_bodegas)
              VALUES(002, 'Maipu', 4);
    INSERT INTO destino(cod_destino, ciudad, num_bodegas)
              VALUES(011, 'Viña del Mar', 5);
    INSERT INTO destino(cod_destino, ciudad, num_bodegas)
              VALUES(041, 'La Serena', 9);
    INSERT INTO destino(cod_destino, ciudad, num_bodegas)
              VALUES(071, 'Talca', 7);
    /*--------------------------------------------------*/          
    INSERT INTO bodegas(cod_bodega, direccion, capacidad)
              VALUES(00011, 'Iquique 341', 10000);          
    INSERT INTO bodegas(cod_bodega, direccion, capacidad)
              VALUES(00021, 'Hugo Ercilla 15', 12000);
    INSERT INTO bodegas(cod_bodega, direccion, capacidad)
              VALUES(00022, 'Olimpo 912', 9000);
    INSERT INTO bodegas(cod_bodega, direccion, capacidad)
              VALUES(00031, 'Jupiter 11', 9500);
    INSERT INTO bodegas(cod_bodega, direccion, capacidad)
              VALUES(00032, '5 de Abril 512', 20000);
    INSERT INTO bodegas(cod_bodega, direccion, capacidad)
              VALUES(00033, 'Manuel Rodriguez', 15000);
    /*-----------------------------------------------------*/
    INSERT INTO destino_bodega(cod_destino, cod_bodega)
              VALUES(001, 00031);
    INSERT INTO destino_bodega(cod_destino, cod_bodega)
              VALUES(001, 00032);          
    INSERT INTO destino_bodega(cod_destino, cod_bodega)
              VALUES(001, 00033);
    INSERT INTO destino_bodega(cod_destino, cod_bodega)
              VALUES(011, 00021);
    INSERT INTO destino_bodega(cod_destino, cod_bodega)
              VALUES(011, 00022);
    INSERT INTO destino_bodega(cod_destino, cod_bodega)
              VALUES(041, 00011);                              
'''

cur.execute(sql)


sql = '''
    INSERT INTO envios(cod_envio, fecha_pedido, fecha_limite)
              VALUES(123, '2019-03-01', '2019-04-01');
    INSERT INTO envios(cod_envio, fecha_pedido, fecha_limite)
              VALUES(124, '2019-03-15', '2019-03-30');          
    INSERT INTO envios(cod_envio, fecha_pedido, fecha_limite)
              VALUES(125, '2019-04-10', '2019-05-20');
    INSERT INTO envios(cod_envio, fecha_pedido, fecha_limite)
              VALUES(126, '2019-05-10', '2019-05-20');
    /*-------------------------------------------------------*/
    
    INSERT INTO productos(cod_producto, marca, tipo)
              VALUES(977, 'Nike', 'Zapatilla');
    INSERT INTO productos(cod_producto, marca, tipo)
              VALUES(980, 'Lancome', 'Perfume');          
    INSERT INTO productos(cod_producto, marca, tipo)
              VALUES(1010, 'LEVIS', 'Pantalon');          
    INSERT INTO productos(cod_producto, marca, tipo)
              VALUES(1011, 'Louis Vuitton', 'Cartera');
    /*-------------------------------------------------------*/
    
    INSERT INTO detalle_envios(cod_envio, cod_producto, cantidad)
              VALUES(123, 977, 500);
    INSERT INTO detalle_envios(cod_envio, cod_producto, cantidad)
              VALUES(123, 1010, 300);                    
    INSERT INTO detalle_envios(cod_envio, cod_producto, cantidad)
              VALUES(125, 977, 700);
    INSERT INTO detalle_envios(cod_envio, cod_producto, cantidad)
              VALUES(126, 980, 1000);
    /*-----------------------------------------------------------
    
    INSERT INTO envio_detalle(cod_envio)
              VALUES(123);
    INSERT INTO envio_detalle(cod_envio)
              VALUES(125);          
    INSERT INTO envio_detalle(cod_envio)
              VALUES(126);
    ----------------------------------------------------------
    
    INSERT INTO producto_detalle(cod_producto)
              VALUES(980);          
    INSERT INTO producto_detalle(cod_producto)
              VALUES(977);          
    INSERT INTO producto_detalle(cod_producto)
              VALUES(1010);          
    ------------------------------------------------------------*/
    
    INSERT INTO envio_camion(cod_envio, patente)
              VALUES(123, 'TR1012');          
    INSERT INTO envio_camion(cod_envio, patente)
              VALUES(125, 'UA6799'); 
    INSERT INTO envio_camion(cod_envio, patente)
              VALUES(126, 'DFPK12'); 
    /*------------------------------------------------------------*/
    
    INSERT INTO envio_chofer(cod_envio, rut)
              VALUES(123, '12025231-8');         
    INSERT INTO envio_chofer(cod_envio, rut)
              VALUES(125, '7845111-4');          
    INSERT INTO envio_chofer(cod_envio, rut)
              VALUES(126, '10111222-4'); 
    /*------------------------------------------------------------*/
    
    INSERT INTO envio_destino(cod_envio, cod_destino)
              VALUES(123, 001);
    INSERT INTO envio_destino(cod_envio, cod_destino)
              VALUES(125, 002);                    
    INSERT INTO envio_destino(cod_envio, cod_destino)
              VALUES(126, 041);            
                                                              
'''

cur.execute(sql)

conexion.commit()

cur.close()

conexion.close()