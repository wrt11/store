list1 = []
while len(list1) < 10:
    list1.append(int(input("请输入数字:")))
    print(list1)
print("十个数的和为:", sum(list1))



list = []
sum = 0
sum1 = 0
for num in range(10):
     number = int(input("请输入一个数（连续10次）:"))
     list.append(number)
     sum += number
     for count in range(len(list)):
         if list[count] > sum1 :
             sum1 = list[count]
         elif list[count] < sum1:
             sum1 = sum1
         elif list[count] == sum1:
             sum1 = list[count]
sum2 = sum/10

print("输入10个数之和为:",sum)
print("输入的10个数中最大的值为:", sum1)
print("输入的10个数的平均值为:",sum2)