import sqlite3
from hashlib import sha256

conexion = sqlite3.connect("tabla_api_juego")
cursor = conexion.cursor()

"""cursor.execute('''CREATE TABLE Personajes(name VARCHAR,
                                        energy INTEGER, 
                                        hungry INTEGER, 
                                        heat INTEGER, 
                                        clean INTEGER, 
                                        happiness INTEGER, 
                                        health INTEGER, 
                                        strenght INTEGER, 
                                        inteligence INTEGER, 
                                        charisma INTEGER, 
                                        luck INTEGER, 
                                        greenleaves INTEGER, 
                                        habilities VARCHAR, 
                                        profession VARCHAR, 
                                        wearing VARCHAR, 
                                        inventory VARCHAR, 
                                        eth wallet INTEGER, 
                                        green leaves wallet INTEGER, 
                                        posX INTEGER,
                                        posY INTEGER)''')"""

cursor.execute("INSERT INTO Personajes VALUES('juan',100,0,32,100,100,100,100,100,100,15,0,'velocidad de movimiento','carpintero','mameluco',0,0,0,0,0)")

conexion.commit()
conexion.close()