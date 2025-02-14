import logging
import socket
import threading
import asyncio
import os 
import sys
import time
#Necesito crear una funcion para intentar la conexion unas 3 veces sino, dar error
#Utilizar variable conn = None
#Utilizar variable retry_count = 5, para intentar la conexion al menos 5 veces
#Client implementation tiene que se accesible desde main.py tambien
#Tengo que poner setear tcp socket desde el mismo binario y otra terminal
#Conectarme desde otra maquina/terminal

class ClientSocket():
    def __init__(self,ip_addressi="127.0.0.1", port=4444):
        self.ip_address = ip_address        #Connection IP
        self.port = port                    #Connection Port
        #Globabl vars
        self.conn = False                   #Check connection
        self.loop = asyncio.get_event_loop()#Value del loop asyncio
        self.c = None
    
    def set_client(self):
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_connection(self):
        conn_count = 5
        try:
            while conn_count > 0:
                try:
                    self.c.connect((self.ip_address, self.port))
                    self.conn = True
                    print(f"Connection with ({self.ip_address},{self.port}) successful.")
                    break
                except socket.error as e:
                    conn_count -= 1
                    print(f"Retrying connection with ({self.ip_address},{self.port}) in 2 seconds. Remaining Attempts: {conn_count}.")
                    logging.error(f"Error: {e}")
                    time.sleep(2)
        except Exception as e:
            logging.warning(f"Could not stablish connection with: ({self.ip_address},{self.port})")
            logging.error(str(e))
            self.conn = False

    def execute_command(self,command):
        pass
    async def __execute_command(self,command):
        pass
