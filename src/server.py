import logging
import socket
import threading
import asyncio
import os 
import sys
import time
import subprocess

#En el caso de hacer las implementaciones de IPv6 
#Cambiar en tcp_server y en udp_server: AF_INET -> AF_INET6
def tcp_server(ip_address,port,delay=None): #Necesito delay en estas funciones???
    #When calling 
    #s = tcp_server(ip_address,port)
    #c = s.accept()
    #Check how yo set up and manage client connections with syncio instead of threads
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("ip_address",port))
    return s
def udp_server(ip_address, port,delay=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

async def cmd_handler(s):
    cmd = await s.recv(1024)
    (exitcode, output) = subprocess.getstatusoutput(cmd.decode('utf-8')) 
    print(f"CMD> {output}")

    await s.send(str(exitcode).encode('utf-8'))
async def handle_client(s): #Tengo que implementar un handler para udp??
                            #En vez de hacer 2 implementaciones, usar recvfrom
                            #En el caso tcp ignoro var addr
                            #En caso udp puedo usarla
                            
    try:
        await data = s.recv(1024).decode('utf-8')
        print(data)
    except OSError as e:
        logging.error(f'Error handling client data: {e}')
    finally:
        s.close()
def send_data(s): 
    try:
        data = input()
        s.send(data.encode("utf-8")
    except OSError as e:
        logging.error(f'Error sending data to client: {e}')

async def receive_udp(s):
    try:
        await data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print(f"{data}")
        return addr
    except OSError as e:
        logging.error(f"Error handling udp client data: {e}")

def send_udp(s,addr):
    try:
        data = input()
        s.sendto(data.encode('utf-8'), addr)
    except OSError as e:
        logging.error(f"Error sending data to udp client: {e}")
   
