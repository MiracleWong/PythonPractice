#!/usr/bin/env python3
from fabric.api import *

env.user='sdnnetconf'
env.hosts=['115.233.240.47']
env.password='SDN_conf@2018'


def remote_task():
    run("ping -a 115.233.240.47 61.130.240.19")
