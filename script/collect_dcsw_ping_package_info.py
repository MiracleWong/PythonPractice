#!/usr/bin/env python3
from fabric import Connection
from time import sleep, ctime
import sys
import csv
import click
import socket
import setting



def get_dcsw_info(f, city):
    package_ping_unavailable_data = []
    if setting.area_info[city]["enabled"]:
        click.echo("回Ping  %s 的机器" % setting.area_info[city]["name_zh_CN"])
        vsw_list = setting.area_info[city]["vsw_info"]
        dcsw_list = setting.area_info[city]["dcsw_info"]
        username = setting.area_info[city]["username"]
        password = setting.area_info[city]["password"]
        vsw_ip = vsw_list[0]
        for dcsw_ip in dcsw_list:
            click.echo("vsw地址为：%s " % vsw_ip)
            click.echo("dcsw地址为：%s " % dcsw_ip)
            host = username + '@' + dcsw_ip
            click.echo("Host地址为：%s " % host)
            ping_package_cmd = "ping -f -s 1523 -a  %s %s" % (dcsw_ip, vsw_ip)
            click.echo("大包package 回ping 命令为：%s " % ping_package_cmd)
            try:
              conn = Connection(host, connect_timeout=15, connect_kwargs={"password": password})
              info_package = conn.run(ping_package_cmd,warn=True)
              click.echo(type(info_package))
              if "Request time out" in str(info_package):
                package_ping_unavailable_data.append(dcsw_ip)
              f.write(str(info_package).encode())
            except socket.timeout as e:
                click.echo("连接超时，请排查DCSW是否开通")
                print(e)
                continue
            conn.close()
        click.echo(package_ping_unavailable_data)
        with open("package_ping_unavailable.csv", "w", newline='') as csvfile:
            for i in package_ping_unavailable_data:
                csvfile.write(i)
                csvfile.write('\n')
        return
    else:
        click.echo("%s 未开通DCSW路由配置" % setting.area_info[city]["name_zh_CN"])
        return

def get_all_machine():
    pass

@click.command()
@click.option("--city", prompt="地区名称，拼音缩写", help="quz hangz huz jiax ningb shaox taiz wenz lis jinh zhous all")
def ping(city):
    if city == "quz" or city == "quzhou":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "hangz" or city == "hangzhou":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "huz" or city == "huzhou":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "jiax" or city == "jiaxing":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "ningb" or city == "ningbo":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "shaox" or city == "shaoxing":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "taiz" or city == "taizhou":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "wenz" or city == "wenzhou":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "lis" or city == "lishui":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "jinh" or city == "jinhua":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "zhous" or city == "zhoushan":
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f,city)
    elif city == "all":
        city_list = ["quz","hangz","huz","jiax","ningb","shaox","taiz","wenz","lis","jinh","zhous"]
        for i in city_list:
            click.echo(i)
            with open('ping.log', 'wb+') as f:
                get_dcsw_info(f,i)


def main():
    dcsw_list = []
    vsw_ip = "61.174.195.75"
    with open('dcsw_cfg.csv','r') as csvfile:
        dcsw_cfg = csv.reader(csvfile)
        for row in dcsw_cfg:
            print(row[0])
            dcsw_list.append(row[0])
    with open('ping.log', 'wb+') as dcsw_cfg_f:
        get_dcsw_info(dcsw_cfg_f, dcsw_list, vsw_ip)

    ## 如果服务器配置了ssh免密码登录，就不需要 connect_kwargs 来指定密码
    #conn = Connection("sdnnetconf@115.233.240.47", connect_kwargs={"password": "SDN_conf@2018"})
    #conn.run("ping -a 115.233.240.47 61.130.240.19",warn=True)
    #conn.run("quit",warn=True)
    #conn.close()

if __name__ == '__main__':
    ping()
