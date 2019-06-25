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



    return render_template("index.html", choferSueldo=choferSueldo)


if __name__=="__main__":
    app.run(debug=True)
