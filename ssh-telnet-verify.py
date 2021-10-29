#!/usr/bin/python3
# coding: utf-8

import sys
import socket
import ipaddress
from datetime import datetime
from datetime import date
print("Verify Default - Telnet e SSH")
iprange = input("Adicione o Range de Rede?  ")
iprangenetwork=ipaddress.ip_network(iprange)
print("-" * 50)
print("Scan Alvo:  " + iprange)
for x in iprangenetwork.hosts():
    target=0
    s=0
    target = ipaddress.ip_address(x)
    strtarget=str(target)
    print("-" * 50)
    print("Scan para o Server: " + strtarget)
    for port in range(22,23):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((strtarget,port))
        banner = s.recv(1024)
        if result ==0:
            print("Port {} está aberta".format(port))
            print(banner)
            s.close()
