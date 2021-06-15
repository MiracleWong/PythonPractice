#!/usr/bin/env python3
from fabric import Connection
from time import sleep, ctime
import sys
import csv
import click
import socket
import setting
import pandas


def get_dcsw_info(f, city, df_city):
    package_ping_unavailable_data = []
    if setting.area_info[city]["enabled"]:
        click.echo("回Ping  %s 的机器" % setting.area_info[city]["name_zh_CN"])
        city_name = setting.area_info[city]["name"]
        vsw_list = setting.area_info[city]["vsw_info"]
        dcsw_list = df_city['mgmt_ip']
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
            # 线下测试导入数据，进行屏蔽
            # try:
            #   conn = Connection(host, connect_timeout=15, connect_kwargs={"password": password})
            #   info_package = conn.run(ping_package_cmd,warn=True)
            #   click.echo(type(info_package))
            #   if "Request time out" in str(info_package):
            #     package_ping_unavailable_data.append(dcsw_ip)
            #   f.write(str(info_package).encode())
            # except socket.timeout as e:
            #     click.echo("连接超时，请排查DCSW是否开通")
            #     print(e)
            #     continue
            # conn.close()
        # click.echo(package_ping_unavailable_data)
        # with open("package_ping_unavailable.csv", "w", newline='') as csvfile:
        #     for i in package_ping_unavailable_data:
        #         csvfile.write(i)
        #         csvfile.write('\n')
        return
    else:
        click.echo("%s 未开通DCSW路由配置" % setting.area_info[city]["name_zh_CN"])
        return


def get_all_machine():
    pass


@click.command()
@click.option("--city", prompt="地区名称，拼音缩写",
              help="quzhou hangzhou huzhou jiaxing ningbo shaoxing taizhou wenzhou lishui jinhua zhoushan all")
def ping(city):
    df = read_csv()

    if city != "all":
        city_code = setting.area_info[city]["area_code"]
        df_city = df.loc[df['dev_addr'] == city_code]
        print(df_city)
        with open('ping.log', 'wb+') as f:
            get_dcsw_info(f, city, df_city)
    else:
        city_list = ["quzhou", "hangzhou", "huzhou", "jiaxing", "ningbo", "shaoxing", "taizhou", "wenzhou", "lishui",
                     "jinhua", "zhoushan"]
        for i in city_list:
            click.echo(i)
            city_code = setting.area_info[i]["area_code"]
            df_city = df.loc[df['dev_addr'] == city_code]
            # 进行屏蔽
            with open('ping.log', 'wb+') as f:
                get_dcsw_info(f, i, df_city)


def main():
    dcsw_list = []
    vsw_ip = "61.174.195.75"
    with open('dcsw_cfg.csv', 'r') as csvfile:
        dcsw_cfg = csv.reader(csvfile)
        for row in dcsw_cfg:
            print(row[0])
            dcsw_list.append(row[0])
    with open('ping.log', 'wb+') as dcsw_cfg_f:
        get_dcsw_info(dcsw_cfg_f, dcsw_list, vsw_ip)

    ## 如果服务器配置了ssh免密码登录，就不需要 connect_kwargs 来指定密码
    # conn = Connection("sdnnetconf@115.233.240.47", connect_kwargs={"password": "SDN_conf@2018"})
    # conn.run("ping -a 115.233.240.47 61.130.240.19",warn=True)
    # conn.run("quit",warn=True)
    # conn.close()


# 读取csv


def read_csv():
    # df = pandas.read_csv("device_no_header.csv")
    df = pandas.read_csv("../device.csv")
    # 按照指定列进行排序
    # list_custom = ['0570', '0571', '0572', '0573', '0574', '0575', '0576', '0577', '0578', '0579', '0580', '057X']
    df = df.sort_values(axis=0, ascending=True, by='dev_addr')
    return df


if __name__ == '__main__':
    ping()
