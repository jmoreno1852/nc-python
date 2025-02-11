import logging
import socket
import threading
import asyncio
import os 
import sys

#En el caso de hacer las implementaciones de IPv6 
#Cambiar en tcp_server y en udp_server: AF_INET -> AF_INET6
def tcp_server(ip_address,port):
    #When calling 
    #s = tcp_server(ip_address,port)
    #c = s.accept()
    #Check how yo set up and manage client connections with syncio instead of threads
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("ip_address",port))
    return s
def udp_server(ip_address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


