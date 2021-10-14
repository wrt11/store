name = [["曹操", "56", "男", "106", "IBM", 500, "50"],
        ["大乔", "19", "女", "230", "微软", 501, "60"],
        ["小乔", "19", "女", "210", "Oracle", 600, "60"],
        ["许褚", "45", "男", "230", "Tencent", 700, "10"]]
name1 = 0
for i in range(4):
    name1 += name[i][5]
print("平均薪资为", round(name1 / 4))
name2 = 0
for i in range(4):
    name2 += int(name[i][1])
print("平均年龄为", round(name2 / 4))
name.append(["刘备", "45", "男", "220", "alibaba", "500", "30"], )
print(name)

name3 = [['罗恩', 23, 35, 44],
         ['哈利', 60, 77, 68, 88, 90],
         ['赫敏', 97, 99, 89, 91, 95, 90],
         ['马尔福', 100, 85, 90]]
for i in range(len(name3)):
    name4 = 0
    for j in range(1,len(name3)):
        name4 += name3[i][j]
    print(name3[i][0], '的总成绩为', name4)
a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)