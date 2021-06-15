#!/usr/bin/env python3
import pexpect
import sys

child = pexpect.spawn('ssh sdnnetconf@115.233.240.47')
fout=file('pexpect.log','w')
child.logfile = fout
#child.logfile = sys.stdout
password='SDN_conf@2018'
child.expect('password:')
child.sendline("SDN_conf@2018")
child.expect('>')
child.sendline("ping -a 115.233.240.47 61.130.240.19")
child.expect('>')
