import logging
import socket
import threading
import asyncio
import os 
import sys
#Necesito crear una funcion para intentar la conexion unas 3 veces sino, dar error
#Utilizar variable conn = None
#Utilizar variable retry_count = 5, para intentar la conexion al menos 5 veces
#Client implementation tiene que se accesible desde main.py tambien
#Tengo que poner setear tcp socket desde el mismo binario y otra terminal
#Connectarme desde otra maquina/terminal
class ClientSocket():
    def __init__(self,ip_address, port):
        self.ip_address = ip_address
        self.port = port
        #Globabl vars
        self.conn = None
        self.loop = asyncio.get_event_loop()
    def get_connection(self):
        pass
    def execute_command(self,command):
        pass
    async def __execute_command(self,command):
        pass
