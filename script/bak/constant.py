#!/usr/bin/env python
# encoding: utf-8

# 已经处理队列的key失效时间, 分钟, 默认为30分钟
done_expire_time = 30
# 设备修复异常的次数
area_abnormal_count = 2
# 设备修复正常时间, 默认单位为秒
normal_recover_time = 20

SUPPER_APP_ID = "a4277dca816ddc8ec207"

# 中心redis
center_redis_info = {
    "host": "172.20.130.103",
    "port": "6377",
    "passwd": "gckq0tG3bP"
}
# 边缘redis
side_redis_info = {
    "port": "6379",
    "passwd": "OedivCL",
}

hz_node_code = ("33010001")

# 中心数据库
center_database_info = {
    # "host": "172.20.130.67",
    # "port": 8066,
    # "host": "172.20.130.62",
    "host": "172.20.130.63",
    "port": 3306,
    "user": "DBcenter",
    "passwd": "root@2016",
    "database": "awifi_capacity"
}

#
center_scheduler_info = {
    "host": "172.24.5.166",
    "port": 31602
}

headers = {
    "Content-Type": "application/json"
}

node_info = {
    "33010001": {
        "name": "hangzhou_1",
        "coop_info": {
            # "host": "172.53.30.1",
            "host": "183.134.201.193",
            "port": 5080
        },
        "redis_info": {
            # "host": "172.53.30.177",
            # "passwd": "st8evLW3",
            # "port": 6377,
            # "db": 8
            "host": "183.134.201.193",
            "passwd": "st8evLW3",
            "port": 5080,
            "db": 8
        },
        "pss_cMain_info": ["172.53.30.8", "172.53.30.10", "172.53.30.12"],
    },
    "33010002": {
        "name": "hangzhou_2",
        "coop_info": {
            # "host": "183.134.201.194",
            "host": "172.53.30.2",
            "port": 5080
        },
        "redis_info": {
            "host": "172.53.30.178",
            "passwd": "st8evLW3",
            "port": 6377,
            "db": 9
            # "host": "183.134.201.194",
            # "passwd": "st8evLW3",
            # "port": 5080,
            # "db": 8
        },
        "pss_cMain_info": ["172.53.30.13", "172.53.30.15", "172.53.30.17"],
    },
    "330200": {
        "name": "ningbo",
        "host": "172.56.30.3",
        "coop_info": {
            "host": "172.56.30.3",
            "port": 5080
        },
        "redis_info": {
            "host": "172.56.30.3",
            "passwd": "OedivCL",
            "port": 6379,
            "db": 8
        },
        "pss_cMain_info": ["172.56.30.11", "172.56.30.13", "172.56.30.15", "172.56.30.17", "172.56.30.19",
                           "172.56.30.21", "172.56.30.23", "172.56.30.25", "172.56.30.27", "172.56.30.29"],
    },
    "33030001": {
        "name": "wenzhou_1",
        "coop_info": {
            "host": "172.59.30.1",
            "port": 5080
        },
        "redis_info": {
            "host": "172.59.30.35",
            "passwd": "st8evLW3",
            "port": 6377,
            "db": 9

        },
        "pss_cMain_info": ["172.59.30.5", "172.59.30.7", "172.59.30.9"],
    },
    # "33040001": {
    #     "name": "jiaxing_1",
    #     "coop_info": {
    #         "host": "172.62.30.93",
    #         "port": 5080
    #     },
    #     "redis_info": {
    #         "host": "172.62.30.121",
    #         "passwd": "st8evLW3",
    #         "port": 6377,
    #         "db": 9
    #     },
    # },
    "330400": {
        "name": "jiaxing",
        "coop_info": {
            "host": "172.62.30.1",
            "port": 5080
        },
        "redis_info": {
            "host": "172.62.30.1",
            "passwd": "OedivCL",
            "port": 6379,
            "db": 9
        },
        "pss_cMain_info": ["172.62.30.3", "172.62.30.5", "172.62.30.20", "172.62.30.78", "172.62.30.79",
                           "172.62.30.80"],
    },
    "33040001": {
        "name": "jiaxing_1",
        "coop_info": {
            "host": "172.62.30.93",
            "domain_name": "jiax-one-sip-server",
            "port": 5080
        },
        "redis_info": {
            "host": "172.62.30.121",
            "passwd": "st8evLW3",
            "port": 6377,
            "db": 9
        },
    },
    "33040002": {
        "name": "jiaxing_2",
        "coop_info": {
            "host": "172.62.30.6",
            "domain_name": "jiax-two-sip-server",
            "port": 5080
        },
        "redis_info": {
            "host": "172.62.32.37",
            "passwd": "st8evLW3",
            "port": 6377,
            "db": 9
        },
    },
    "33040003": {
        "name": "jiaxing_3",
        "coop_info": {
            "host": "172.62.30.62",
            "domain_name": "jiax-three-sip-server",
            "port": 5080
        },
        "redis_info": {
            "host": "172.62.32.93",
            "passwd": "st8evLW3",
            "port": 6377,
            "db": 9
        },
    },
    "33040004": {
        "name": "jiaxing_4",
        "coop_info": {
            "host": "172.62.30.118",
            "domain_name": "jiax-four-sip-server",
            "port": 5080
        },
        "redis_info": {
            "host": "172.62.32.149",
            "passwd": "st8evLW3",
            "port": 6377,
            "db": 9
        },
    },
    "330500": {
        "name": "huzhou",
        "coop_info": {
            "host": "172.65.30.1",
            "port": 5080
        },
        "redis_info": {
            "host": "172.65.30.1",
            "passwd": "OedivCL",
            "port": 6379,
            "db": 8
        },
        "pss_cMain_info": ["172.65.30.5", "172.65.30.6", "172.65.30.8", "172.65.30.10", "172.65.30.54", "172.65.30.55",
                           "172.65.30.105", "172.65.30.106", "172.65.30.129", "172.65.30.130", "172.65.30.131",
                           "172.65.30.132"],
    },
    "330600": {
        "name": "shaoxing",
        "coop_info": {
            "host": "172.62.30.1",
            "port": 5080
        },
        "redis_info": {
            "host": "172.62.30.1",
            "passwd": "OedivCL",
            "port": 6379,
            "db": 9
        },
        "pss_cMain_info": ["172.62.30.3", "172.62.30.5", "172.62.30.20"],
    },
    "330700": {
        "name": "jinhua",
        "coop_info": {
            "host": "172.65.30.1",
            "port": 5080
        },
        "redis_info": {
            "host": "172.65.30.1",
            "passwd": "OedivCL",
            "port": 6379,
            "db": 8
        },
        "pss_cMain_info": ["172.65.30.5", "172.65.30.6", "172.65.30.8", "172.65.30.10"],
    },
    "33070001": {
        "name": "jinhua_1",
        "coop_info": {
            "host": "172.83.158.1",
            "domain_name": "jinh-one-sip-server",
            "port": 5080
        },
        "redis_info": {
            "host": "172.83.158.30",
            "passwd": "st8evLW3",
            "port": 6377,
            "db": 9
        },
    },
    "33070002": {
        "name": "jinhua_2",
        "coop_info": {
            "host": "172.83.158.106",
            "domain_name": "jinh-two-sip-server",
            "port": 5080
        },
        "redis_info": {
            "host": "172.83.158.136",
            "passwd": "st8evLW3",
            "port": 6377,
            "db": 9
        },
    },
    "330800": {
        "name": "quzhou",
        "coop_info": {
            "host": "172.74.30.3",
            "port": 6018
        },
        "redis_info": {
            "host": "172.74.30.3",
            "passwd": "OedivCL",
            "port": 6379,
            "db": 8
        },
        "pss_cMain_info": ["172.74.30.10", "172.74.30.15", "172.74.30.17", "172.74.30.24", "172.74.30.22",
                           "172.74.30.23", "172.74.30.25", "172.74.30.26", "172.74.30.107", "172.74.30.99",
                           "172.74.30.103", "172.74.30.133", "172.74.30.134", "172.74.30.135", "172.74.30.136",
                           "172.74.30.137", "172.74.32.19", "172.74.32.20", "172.74.32.21", "172.74.32.22",
                           "172.74.32.23", "172.74.32.24"],
    },
    "330900": {
        "name": "zhoushan",
        "coop_info": {
            "host": "172.77.30.1",
            "port": 5080
        },
        "redis_info": {
            "host": "172.77.30.1",
            "passwd": "OedivCL",
            "port": 6379,
            "db": 8
        },
        "pss_cMain_info": ["172.77.30.3", "172.77.30.4", "172.77.30.6", "172.77.30.104", "172.77.30.105"],
    },
    "331000": {
        "name": "taizhou",
        "coop_info": {
            "host": "172.68.30.1",
            "port": 5080
        },
        "redis_info": {
            "host": "172.68.30.1",
            "passwd": "OedivCL",
            "port": 6379,
            "db": 8
        },
        "pss_cMain_info": ["172.68.30.2", "172.68.30.11", "172.68.30.6", "172.68.30.8", "172.68.30.77", "172.68.30.78",
                           "172.68.30.79", "172.68.30.89", "172.68.30.90", "172.68.30.91", "172.68.30.114",
                           "172.68.30.115", "172.68.30.116"],
    },
    "331100": {
        "name": "lishui",
        "coop_info": {
            "host": "172.71.30.1",
            "port": 5080
        },
        "redis_info": {
            "host": "172.71.30.1",
            "passwd": "OedivCL",
            "port": 6379,
            "db": 8
        },
        "pss_cMain_info": ["172.71.30.3", "172.71.30.6"],
    }
}
