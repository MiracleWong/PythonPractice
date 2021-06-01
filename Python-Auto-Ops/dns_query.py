#!/usr/bin/python3
# -*- coding: UTF-8 -*

import dns.resolver
import httplib2

domain = 'www.baidu.com'  #定义业务域名
iplist = []  #定义域名ip列表

def get_iplist(domain): #定义解析函数，解析成功IP将被追加到iplist
    try:
        A = dns.resolver.resolve(domain,'A') #解析a记录类型
    except Exception as e:
        print("dns resolver error:"+str(e))
        return False
    for i in A:
        iplist.append(i) #追加到iplist
    return True

def checkip(iplist):
    for ip in iplist:
        checkurl = str(ip)+":80"
        getcontent = ""
        httplib2.socket.setdefaulttimeout(5)  #定义http连接超时时间（5秒）
        conn = httplib2.HTTPConnectionWithTimeout(checkurl) #创建http连接对象

        try:
            conn.request("GET","/",headers={"HOST":domain}) #发起URL请求，添加host主机头
            r = conn.getresponse()
            getcontent = r.read(15)  #获取URL页面前15个字符，以便做可用性校验
        finally:
            if getcontent==b"<!DOCTYPE html>":
                print(str(ip)+"[OK]")
            else:
                print(str(ip)+"[ERROR]")

if __name__ == '__main__':
    if get_iplist(domain) and len(iplist) > 0:
        checkip(iplist)
    else:
        print('dns resolve error。')
