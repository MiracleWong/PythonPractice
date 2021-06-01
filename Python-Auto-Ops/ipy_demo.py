#!/usr/bin/python
# -*- coding: UTF-8 -*-

from IPy import IP

ip = IP('192.168.0.0/24')
print(ip.len())
# for i in ip:
#     print(i)

ip = IP('192.168.1.20')
print(ip.iptype())
print(IP('8.8.8.8').iptype())
print(IP('8.8.8.8').int())
print(IP('8.8.8.8').strHex())
print(IP('8.8.8.8').strBin())
print(IP(0x8080808))
print(IP('192.168.10.0/24').strNormal())
print(IP('192.168.10.0/24').strNormal(0))
print(IP('192.168.10.0/24').strNormal(1))
print(IP('192.168.10.0/24').strNormal(2))
print(IP('192.168.10.0/24').strNormal(3))

