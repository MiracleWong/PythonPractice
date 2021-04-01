

sorted_list = sorted([30, 50, 20, 10, 40])
print(sorted_list)
# [10, 20, 30, 40, 50]

sorted_list2 = sorted(["a", str(1), "bb"])
print(sorted_list2)

list3 = ["a", "c", "bb"]
no_value = list3.sort()
print(list3)
# ['a', 'bb', 'c']  执行结果
print(no_value)
# None  执行结果

# sort() （函数会直接修改当前列表这种修改称作“原地修改”），并返回一个空值 None。
# sorted() 函数不会对原有的列表进行修改，它会把排序好的结果存入到一个新的列表当中。


sorted_list4 = sorted([30, 50, 20, 10, 40], reverse=True)
print(sorted_list4)
print(sorted_list4[:3])
# [50, 40, 30]

student_dict1 = {'Jerry':'1003',
                 'Tom':'1005',
                 'Beta':'2001',
                 'Shuke':'2003'
}

# 输出字典的键和值
print(student_dict1.items())
# dict_items([('Jerry', '1003'), ('Tom', '1005'), ('Beta', '2001'), ('Shuke', '2003')])

# 按照字典的键排序
print(sorted(student_dict1.items(), key=lambda d: d[0]))
# [('Beta', '2001'), ('Jerry', '1003'), ('Shuke', '2003'), ('Tom', '1005')]

# 按照字典的值排序
result = sorted(student_dict1.items(), key=lambda d: d[1])
print(result)
# [('Jerry', '1003'), ('Tom', '1005'), ('Beta', '2001'), ('Shuke', '2003')]
# 将结果转换为字典
print(dict(result))
# {'Jerry': '1003', 'Tom': '1005', 'Beta': '2001', 'Shuke': '2003'}