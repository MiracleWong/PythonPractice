#!/usr/bin/env python3
import paramiko

hostname='115.233.240.47'
username='sdnnetconf'
password='SDN_conf@2018'
paramiko.util.log_to_file('paramiko.log')

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('ping -a 115.233.240.47 61.130.240.19')
print(stdout.read())
ssh.close()
