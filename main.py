"""

判断：
 单分支 if   eles
 多分支 if  elif   elif  elif ...... else
10-90这个范围里面
如果猜大了打印”猜大了“ 猜小了
最多猜3次 锁屏 time.sleep(10)
"""
import random
import time

randint = random.randint(10, 90)  # 从10到90之前随机取一个数字
num1 = randint
cout = 0
print("3次机会猜大小")
while True:
    cout = cout + 1
    num = int(input("请输入一个数字"))
    if num1 == num:
        print("猜对了")
        break
    elif num1 > num and cout < 3:
        print("猜小了")
    elif num1 < num and cout < 3:
        print("猜大了")
    elif num1 != num and cout == 3:
        print("将在10秒后锁屏")
        time.sleep(10)
        break
