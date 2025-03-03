import logging
import socket
import threading
import asyncio
import os 
import sys
import time
import ctypes
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
    def get_data(self):
        try:
            data = self.c.recv(1024).decode('utf-8')
            return data
        except InterruptedError as e:
            logging.error(f"Client Get Error!!! {e}")
            return None
        except OSError as e:
            logging.error(f"Client Get Error!!! {e}")
            return None
    def send_data(self, delay=None):
        try:
            data = input()
            if data != "":
                self.c.send(data.encode('utf-8'))
            else:
                print("Cant send empty strings")
        except InterruptedError as e:
            logging.error(f"Client Send Interrupted!!! {e}")
        except OSError as e:
            logging.error(f"Client Send Interrupted!!! {e}")
    ###-e implementation
    def execute_command(self,command):
        try:
            return self.loop.run_until_complete(self.__execute_command(command)
        except Exception as e:
            logging.warning(f"Failed to execute {command =}.")
        return False
    async def __execute_command(self,command):
        if self.conn is None:
            logging.debug(f"Connection object is None. Creating connection with {self/URL}")
            self.conn = await self.get_connection()
        await self.conn.send(command)
        return await self.conn.recv()
    def num_host(addr): #-n Implementation
        try:
            socket.inet_pton(socket.AF_INET, address)
            return True
        except socket.error:
            logging.warning(f"{addr} is not valid for IPv4")
            return False

    def log_data(file,data): #-o Implementation
        try:
            with open(file,"a") as f:
                f.write(f"{data}")
        except IOError as e:
            logging.error(f"Error when writting file {file}: {e}")

    def enable_md5sig(self): #-S Implementation
        TCP_MD5SIG = 14
        IPPROTO_TCP = 6
        libc = ctypes.cdll.LoadLibrary("libc.so.6")
        
        try:
            socket_file = self.c.fileno()
        except Exception as e:
            logging.warning(f"Error getting socket file number: {e}")
            return
        libc.setsockopt(socket_file,IPPROTO_TCP,TCP_MD5SIG, b'')
        logging.info("Sock option stablished to TCP_MD5SIG")

















