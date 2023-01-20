import sqlite3
from hashlib import sha256

conexion = sqlite3.connect("tabla_api_juego")
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE Login(Usuario VARCHAR UNIQUE, Contraseña VARCHAR PRIMARY KEY, Address VARCHAR )''')



productos = [
    ("Usuario1", sha256('password1'.encode('utf-8')).hexdigest(), "0x"+sha256('password1'.encode('utf-8')).hexdigest()),
    ("Usuario2", sha256('password2'.encode('utf-8')).hexdigest(), "0x"+sha256('password2'.encode('utf-8')).hexdigest()),
    ("Usuario3", sha256('password3'.encode('utf-8')).hexdigest(), "0x"+sha256('password3'.encode('utf-8')).hexdigest()),
    ("Usuario4", sha256('password4'.encode('utf-8')).hexdigest(), "0x"+sha256('password4'.encode('utf-8')).hexdigest())]

cursor.executemany("INSERT INTO Login VALUES(?,?,?)", productos)


conexion.commit()
conexion.close()