import random
print("***********************")
print("*   中国工商银行        *")
print("***********************")
print("*     1、开户          *")
print("*     2、存钱          *")
print("*     3、取钱          *")
print("*     4、转账          *")
print("*     5、查询          *")
print("*     6、再见          *")
print("***********************")
#空字典
bank={123456789: {'username': '1', 'password': '1', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 5000000, 'bank_name': 'M73迪迦银行'}}
#'F': {'account': 98835406, 'password': '1', 'country': '中国', 'porvince': '昌平', 'street': '001', 'door': '001', 'money': 0}
bank_name="M73迪迦银行"
#调用的函数元素是一一对应的，不是名称对应
def bank_add(account,username,password,country,province,street,door):
    if account in  bank:#名字  重名
        return 2
    elif len(bank)>= 100:#大于100个用户
        return 3
    else:#正常添加用户
        bank[account]={
            "username":username,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1
def Useradd():
    account=random.randint(10000000,99999999)#账号随机产生的
    username=input("请输入您的姓名")
    password=input("请输入你的密码")
    print("下面请输入您的地址：")
    country=input("\t\t请输入你的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    add=bank_add(account,username,password,country,province,street,door)
    if add ==3:
        print("数据库已满，请到光之国银行开户")
    elif add==2:
        print("用户已存在")
    elif add ==1:
        print("恭喜你添加用户成功，以下是您的账户信息：")
        info ='''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))


def Deposit():
    DA = int(input("请输入存钱的账号:"))
    if DA in bank:
        savemoney = int(input("存款金额:"))
        bank[DA]["money"] += savemoney
    else :
        print("输入正确的存款账号")


def Draw():
    withdraw = int(input("请输入取款账号:"))
    if withdraw in bank:
        password = input("请输入账号密码:")
        if password == bank[withdraw]["password"]:
            amount = int(input("请输入你要取出的金额:"))
            if amount <= bank[withdraw]["money"]:
                bank[withdraw]["money"] -= amount
                print("你的余额为:",bank[withdraw]["money"])
                return 0
            else :
                print("你的账户余额不足!")
                return 3
        else :
            print("密码错误!")
            return 2
    else :
        print("账号错误!")
        return 1


def Transfer():
    startaccount = int(input("请输入转入账号:"))
    if startaccount in bank:
        endaccount = int(input("请输入转出账号:"))
        if endaccount in bank:
            Transferamount = int(input("请输入转账金额:"))
            if Transferamount <= bank[endaccount]["money"]:
                bank[endaccount]["money"] -= Transferamount
                bank[startaccount]["money"] += Transferamount
                print("转账成功，你当前的余额为:",bank[endaccount]["money"])
            else:
                print("你的余额不足！")
        else:
            print("输入正确的转出账号")
    else:
        print("输入正确的转入账号")


def Query():
    queryuser = int(input("请输入查询的账号:"))
    if queryuser in bank:
        querypassword = input("请输入账号密码:")
        if querypassword == bank[queryuser]["password"]:
            print("\t\t------信息--------")
            print("\t\t账号:",queryuser)
            for key,value in bank[queryuser].items():
                if key == str("username"):
                    print("\t\t","用户名",":",bank[queryuser]["username"])
                elif key == str("password"):
                    print("\t\t", "密码", ":", bank[queryuser]["password"])
                elif key == str("money"):
                    print("\t\t", "余额", ":", bank[queryuser]["money"])
                elif key == str("bank_name"):
                    print("\t\t", "开户行", ":", bank[queryuser]["bank_name"])
                elif key == str("country"):
                    print("\t\t用户住址",":", bank[queryuser]["country"],bank[queryuser]["province"],bank[queryuser]["street"])
        else:
            print("密码错误！")
    else:
        print("账号错误")


while True:
    index=int(input("请输入您的操作"))
    if index ==1:
        Useradd()
    elif index == 2:
        Deposit()
    elif index == 3:
        Draw()
    elif index == 4:
        Transfer()
    elif index == 5:
        Query()
    elif index == 6:
        exit()
    print(bank)
# def  add():
#     a=int(input("数字"))
#     b=int(input("数字2"))
#     c=a+b
#     if c==10:
#         return 1
# if add(5,5) ==1:
#     print("成功")3
