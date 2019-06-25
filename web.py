from flask import Flask
from flask import render_template, request, redirect
from datosMaster import *
import psycopg2 as psq

conn = psq.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,password))

cur = conn.cursor()

app=Flask(__name__)


@app.route('/')

@app.route('/index')
def index():

    sql="""
    select chofer.rut, chofer.sueldo, chofer.despedido
    from chofer
    where chofer.sueldo>700000;
    """
    cur.execute(sql)
    choferSueldo = cur.fetchall()

    sql ="""
    
    select chofer.nombre, chofer.apellidoP, chofer.rut
    from chofer, chofer_camion
    where chofer.rut = chofer_camion.rut
    and chofer_camion.patente='DFPK12';
    
    """

    cur.execute(sql)
    choferPatente=cur.fetchall()

    sql="""
    select camion.capacidad, camion.patente, camion.empresa
    from camion
    where camion.capacidad = (select max(camion.capacidad) from camion);
    """
    cur.execute(sql)
    camionCapacidad=cur.fetchall()

    sql="""
    select *
    from envios
    order by envios.limite;

    """
    cur.execute(sql)
    envioFecha=cur.fetchall()

    sql="""
    select envios.cod_envio, envios.fecha_pedido
    from envios, detalle_envios, productos
    where envios.cod_envio=detalle_envios.cod_envio
    and detalle_envios.cod_producto=productos.cod_producto
    and productos.marca='Nike';

    """
    cur.execute(sql)
    envioNike=cur.fetchall()

    sql="""
    select camion.patente, camion.fecha_ult_mantencion
    from camion
    order by camion.fecha_ult_mantencion;
    """
    cur.execute(sql)
    camionOrden=cur.fetchall()

    sql="""
    select camion.empresa, SUM(camion.capacidad) as CapacidadTotal
    from camion
    group by camion.empresa;

    """
    cur.execute(sql)
    camionCarga=cur.fetchall()

    sql="""
    select detalle_envios.cod_envio, SUM(detalle_envios.cantidad) as TotalCantidad
    from detalle_envios
    group by detalle_envios.cod_envio;

    """
    cur.execute(sql)
    envioProductos=cur.fetchall()
    return render_template("index.html", choferSueldo=choferSueldo)


if __name__=="__main__":
    app.run(debug=True)
