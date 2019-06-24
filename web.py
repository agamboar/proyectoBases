from app import app
from flask import render_template, request, redirect
from datosMaster import *
import psycopg2 as psq

conn = psq.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,password))

cur = conn.cursor()

@app.route('/')

@app.route('/')