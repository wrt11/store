num = input('请输入十个数，空格隔开：').split()
list = []
for i in num:
    list.append(float(i))
num1 = sum(list) / len(list)
print('这十个数的平均数为：', round(num1, 2))
