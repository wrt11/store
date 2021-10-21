import random

from 工商银行完整版 import bank_saveMoney, bank_takeMoney

print("***********************")
print("*   中国农业银行        *")
print("***********************")
print("*     1、开户          *")
print("*     2、存钱          *")
print("*     3、取钱          *")
print("*     4、转账          *")
print("*     5、查询          *")
print("*     6、再见          *")
print("***********************")

##银行
bank = {123456789: {'username': '1', 'password': '1', 'country': '1', 'province': '1', 'street': '1', 'door': '1',
                    'money': 5000000, 'bank_name': '农业银行'}}
bank_name = "农业银行"


def inputHelp(chose, datatype="str"):
    while True:
        print("请输入", chose, ":")
        i = input(">>>:")
        if len(i) == 0:
            print("该项不能为空！请重新输入！")
            continue
        if datatype != "str":
            return int(i)
        else:
            return i


# 判断是否存在该银行选项
def isExists(chose, data):
    if chose in data:
        return True
    return False


# 通过账号获取账户信息
def findByAccount(account):
    for i in bank.keys():
        if bank[i]["account"] == account:
            return i
    return None


def bank_add(account, username, password, country, province, street, door):
    if account in bank:  # 名字  重名
        return 2
    elif len(bank) >= 100:  # 大于100个用户
        return 3
    else:  # 正常添加用户
        bank[username] = {
            "account": account,
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "money": 0,
            "bank_name": bank_name
        }
        return 1


def useradd():
    account = random.randint(10000000, 99999999)
    username = input("请输入您的姓名")
    password = input("请输入您的密码")
    print("下面请输入您的地址：")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    add = bank_add(account, username, password, country, province, street, door)
    if add == 3:
        print("数据库已满")
    elif add == 2:
        print("用户已存在")
    elif add == 1:
        print("恭喜你添加用户成功，以下是您的账户信息：")
        global myinfo
        myinfo = '''
                    ------------个人信息------------
                    账号:%s
                    用户名：%s
                    密码：*****
                    地址：
                      国籍：%s
                      省份：%s
                      街道：%s
                      门牌号：%s
                    余额：%s
                    开户行名称：%s
                    -------------------------------
                '''
        # 每个元素都可传入%
        print(myinfo % (account, username, country, province, street, door, bank[username]["money"], bank_name))


# 存钱
def saveMoney():
    account = inputHelp("账号")
    m = inputHelp("存入的金额", "int")

    flag = bank_saveMoney(account, m)

    if flag:
        print("存储成功!您的个人信息为：")
        uname = findByAccount(account)
        user = bank[uname]
        print(myinfo.format(account=user["account"],
                            username=uname,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]
                            ))
    else:
        print("对不起，您的个人信息不存在！请先开户后再次操作！")


# 取钱
def takeMoney():
    account = inputHelp("账户")
    password = inputHelp("密码")
    tmoney = inputHelp("取出金额", "int")

    f = bank_takeMoney(account, password, tmoney)

    if f == 1:
        print("改用户不存在！")
    elif f == 2:
        print("密码错误！")
    elif f == 3:
        print("取款金额不足！")
    elif f == 0:
        print("取款成功！")
        bank_selectUser(account, password)


# 银行的转账功能
def bank_transformMoney(outputaccount, inputaccount, outputpassword, outputmoney):
    status = bank_takeMoney(outputaccount, outputpassword, outputmoney)
    if status == 1:
        return status
    elif status == 2:
        return status
    elif status == 3:
        return status

    if inputaccount != None and findByAccount(inputaccount) != None:
        bank_saveMoney(inputaccount, outputmoney)
        return 0
    else:
        return 1


def transformMoney():
    output = inputHelp("转出的账号")
    input = inputHelp("转入的账号")
    outputpass = inputHelp("转出的密码")
    outputmoney = inputHelp("要转出的金额", "int")

    f = bank_transformMoney(output, input, outputpass, outputmoney)

    if f == 1:
        print("转出或转入的账号不存在！")
    elif f == 2:
        print("输入密码错误！")
    elif f == 3:
        print("转账金额不足！")
    else:
        print("转账成功！")
        print("您的个人信息：")
        bank_selectUser(output, outputpass)


# 银行的查询功能
def bank_selectUser(account, password):
    uname = findByAccount(account)

    if uname != None and len(uname) != 0:
        if password == bank[uname]["password"]:
            user = bank[uname]
            print(myinfo.format(account=user["account"],
                                username=uname,
                                password=user["password"],
                                country=user["country"],
                                province=user["province"],
                                street=user["street"],
                                door=user["door"],
                                money=user["money"],
                                bank_name=user["bank_name"]
                                ))
        else:
            print("用户密码错误！")
    else:
        print("该用户不存在！")


def selectUser():
    account = inputHelp("账号")
    password = inputHelp("密码")

    bank_selectUser(account, password)


while True:
    index = int(input("请输入您的操作"))
    if index == 1:
        useradd()
    elif index == 2:
        saveMoney()
    elif index == 3:
        takeMoney()
    elif index == 4:
        transformMoney()
    elif index == 5:
        selectUser()
    elif index == 6:
        exit()
