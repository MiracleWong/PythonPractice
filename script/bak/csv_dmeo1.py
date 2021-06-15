li = ['a','b','c']
with open("demo1.csv", "w", newline='') as csvfile:
    for i in li:
        csvfile.write(i)
        csvfile.write('\n')
