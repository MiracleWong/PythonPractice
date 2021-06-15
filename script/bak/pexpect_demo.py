#!/usr/bin/env python3
from pexpect import pxssh
import getpass
try:
    s = pxssh.pxssh()
    hostname='115.233.240.47'
    username='sdnnetconf'
    password='SDN_conf@2018'
    s.login (hostname, username, password)
    s.sendline ('dir')
    s.prompt()
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh:
    print("pxssh failed on login.")
