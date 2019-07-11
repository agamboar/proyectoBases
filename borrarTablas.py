import psycopg2 as psq
from datosMaster import *

conn = psq.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,password))

cur = conexion.cursor()

sql = """select 'drop table"' || tablename || '" cascade;' from pg_tables;"""

cur.execute(sql)

sql = '''
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

'''

cur.execute(sql)

conexion.commit()

cur.close()

conexion.close()
