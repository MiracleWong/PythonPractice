#!/usr/bin/env python3
from fabric import Connection

hostname='115.233.240.47'
username='sdnnetconf'
password="SDN_conf@2018"
host= username + '@' + hostname
ping_cmd="ping -a 115.233.240.47 61.130.240.19"

def deploy():
    # 如果服务器配置了ssh免密码登录，就不需要 connect_kwargs 来指定密码
    #conn = Connection("sdnnetconf@115.233.240.47", connect_kwargs={"password": password})
    conn = Connection(host, connect_kwargs={"password": password})
    #conn.run("ping -a 115.233.240.47 61.130.240.19",warn=True)
    conn.run(ping_cmd,warn=True)
    #conn.run("quit",warn=True)
    conn.close()

if __name__ == '__main__':
    deploy()
