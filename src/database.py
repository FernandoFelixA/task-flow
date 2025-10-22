import sqlite3  #Modulo de python para interactuar con SQL
from .modelos import Tarea, Proyecto   #Importar desde modelos.py
import os

DATABASE_NAME = 'tareas.db'

def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def crear_tarea(self, tarea: Tarea) -> Tarea:
    conn = get_connection() #Obtener conexion a la DB
    cursor = conn.cursor() #Crear cursor para ejecutar comandos SQL

    cursor.execute("""
        INSERT INTO tareas (titulo, descripcion, fecha_creacion, fecha_limite, prioridad, estado, proyecto_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (tarea._titulo, tarea._descripcion, tarea._fecha_creacion, tarea._fecha_limite, tarea._prioridad, tarea._estado, tarea._proyecto_id)
    )

    Tarea.id = cursor.lastrowid   #POO - SQL - POO: Asignar ID generado por la DB al objeto Tarea
    conn.commit() 
    conn.close()
    return Tarea
