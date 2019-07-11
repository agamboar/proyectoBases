from flask import Flask
from flask import render_template, request, redirect, flash, url_for
from datosMaster import *
import psycopg2 as psq

conn = psq.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,password))
cur = conn.cursor()
cur.execute("ROLLBACK")
conn.commit()

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    sql = """
    select chofer.rut, chofer.sueldo, chofer.despedido
    from chofer
    where chofer.sueldo>700000;
    """
    cur.execute(sql)
    chofer1 = cur.fetchall()

    sql = """
    
    select chofer.nombre, chofer.apellidoP, chofer.rut
    from chofer, chofer_camion
    where chofer.rut = chofer_camion.rut
    and chofer_camion.patente='DFPK12';
    
    """

    cur.execute(sql)
    chofer2 = cur.fetchall()

    sql = """
    select camion.capacidad, camion.patente, camion.empresa
    from camion
    where camion.capacidad = (select max(camion.capacidad) from camion);
    """
    cur.execute(sql)
    camion1 = cur.fetchall()

    sql = """
    select *
    from envios
    order by envios.fecha_limite;

    """
    cur.execute(sql)
    envio1 = cur.fetchall()

    sql = """
    select envios.cod_envio, envios.fecha_pedido
    from envios, detalle_envios, productos
    where envios.cod_envio=detalle_envios.cod_envio
    and detalle_envios.cod_producto=productos.cod_producto
    and productos.marca='Nike';

    """
    cur.execute(sql)
    envio2 = cur.fetchall()

    sql = """
    select camion.patente, camion.fecha_ult_mantencion
    from camion
    order by camion.fecha_ult_mantencion;
    """
    cur.execute(sql)
    camion2 = cur.fetchall()

    sql = """
    select camion.empresa, SUM(camion.capacidad) as CapacidadTotal
    from camion
    group by camion.empresa;

    """
    cur.execute(sql)
    camion3 = cur.fetchall()

    sql = """
    select detalle_envios.cod_envio, SUM(detalle_envios.cantidad) as TotalCantidad
    from detalle_envios
    group by detalle_envios.cod_envio;

    """
    cur.execute(sql)
    envio4 = cur.fetchall()


    return render_template("index.html", chofer1=chofer1, chofer2=chofer2, camion1=camion1, envio1=envio1,
                           envio2=envio2, camion2=camion2, camion3=camion3, envio4=envio4, status=False)


@app.route('/tables')
def tables():

    sql='''
    select * from bodegas;
    '''
    cur.execute(sql)
    bodegas = cur.fetchall()

    sql = '''
        select * from camion;
        '''
    cur.execute(sql)
    camion = cur.fetchall()

    sql = '''
        select * from chofer;
        '''
    cur.execute(sql)
    chofer = cur.fetchall()

    sql = '''
        select * from despedidos;
        '''
    cur.execute(sql)
    despedidos = cur.fetchall()

    sql = '''
        select * from destino;
        '''
    cur.execute(sql)
    destino = cur.fetchall()

    sql = '''
        select * from envios;
        '''
    cur.execute(sql)
    envios = cur.fetchall()

    sql = '''
        select * from productos;
        '''
    cur.execute(sql)
    productos = cur.fetchall()

    sql = '''
        select * from detalle_envios;
        '''
    cur.execute(sql)
    detalle_envios = cur.fetchall()

    sql = '''
        select * from chofer_camion;
        
    '''
    cur.execute(sql)
    chofer_camion= cur.fetchall()

    sql='''
        select * from destino_bodega;
    '''
    cur.execute(sql)
    destino_bodega=cur.fetchall()


    sql='''
        select * from envio_camion;
    '''
    cur.execute(sql)
    envio_camion=cur.fetchall()

    sql = '''
            select * from envio_chofer;
        '''
    cur.execute(sql)
    envio_chofer = cur.fetchall()

    sql = '''
            select * from envio_destino;
        '''
    cur.execute(sql)
    envio_destino = cur.fetchall()
    return render_template("blog.html",detalle_envios=detalle_envios , bodegas=bodegas, camion=camion, chofer=chofer,
                           despedidos=despedidos, destino=destino,
                           envios= envios, productos=productos, chofer_camion=chofer_camion, destino_bodega=destino_bodega, envio_camion=envio_camion,
                           envio_chofer=envio_chofer, envio_destino=envio_destino)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.values.get('usuario')
        pwd = request.values.get('pwd')

        sql = """SELECT COUNT(usuario) FROM usuario
        WHERE usuario = '%s' AND contraseña = '%s'""" % (usuario, pwd)

        cur.execute(sql)
        login = cur.fetchone()
        if 1 in login:
            return redirect('tables')
        else:
            pass
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        usuario = request.values.get('usuario')
        pwd = request.values.get('pwd')
        vpwd = request.values.get('vpwd')
        email = request.values.get('mail')

        if pwd == vpwd:
            sql = """
                        INSERT INTO usuario(usuario, contraseña, mail)
                        VALUES (%s, %s, %s)
                    """ % (usuario, pwd, email)

            cur.execute(sql)
            return redirect('/index', status=True)




    return render_template("register.html")


@app.route('/self_tabla', methods=['POST'])

def self_tabla():
    pass


if __name__ == "__main__":
    app.run(debug=True)
