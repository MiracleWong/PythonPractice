#
# string1="aaa新年快乐bbb"
# string2=string1.replace("新年快乐", "恭喜发财")
# print(string2)
# # aaa恭喜发财bbb
#
# string3="aaa新年快乐bbb新年快乐ccc"
# string4=string3.replace("新年快乐", "恭喜发财", 2)
# print(string4)
#
#
# string5='aaa,."bbb'
# string6=string5.replace(',', '，')
# string6=string6.replace('.', '。')
# string6=string6.replace('"', '“')
# # 需要更多的replace()匹配更多的标点符号
# print(string6)
# # aaa，。“bbb

# 保存映射关系
def replace_city(city_name):
    # 如果字典只使用一次，那也可以不使用字典名称
    return {
        "GUANGDONG": "广东省",
        "HEBEI": "河北省",
        "HUNAN": "湖南省",
        "HANGZHOU": "杭州市",
    }[city_name]


# 根据映射关系批量循环
def replace_multi(my_citys, replaced_string):
    for pin_yin in my_citys:
        replaced_string = replaced_string.replace(pin_yin, replace_city(pin_yin))
    return replaced_string


citys = ("GUANGDONG", "HUNAN")


string1 = """GUANGDONG，简称“粤”，中华人民共和国省级行政区，省会广州。因古地名广信之东，故名“GUANGDONG”。位于南岭以南，南海之滨，与香港、澳门、广西、HUNAN、江西及福建接壤，与海南隔海相望。"""

string2 = replace_multi(citys, string1)
print(string2)