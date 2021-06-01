#!/usr/bin/python
# -*- coding: UTF-8 -*

import dns.resolver

domain = "qq.com"
A = dns.resolver.resolve(domain,'A')
for i in A:
    print(i)

MX = dns.resolver.resolve(domain, 'MX')
for i in MX:
    print(i)

domain2 = "www.qq.com"
CNAME = dns.resolver.resolve(domain2, 'CNAME')
for i in CNAME:
    print(i)