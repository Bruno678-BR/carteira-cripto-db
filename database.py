import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

class DBConnection:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "carteira_investimentos"
        self.connection = None
    
    def connect (self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            if self.connection.is_connected():
                print("Conexão com o MYSQL realizada com sucesso!")
                return self.connection
        except Error as e:
            print(f"Erro ao se conectar ao MYSQL:{e}")
            return None
    
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão com o MYSQL encerrada!")
