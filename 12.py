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
bank={}
#'F': {'account': 98835406, 'password': '1', 'country': '中国', 'porvince': '昌平', 'street': '001', 'door': '001', 'money': 0}
bank_name="M73迪迦银行"
#调用的函数元素是一一对应的，不是名称对应
def bank_add(account,username,password,country,province,street,door):
    if username in  bank:#名字  重名
        return 2
    elif len(bank)>= 100:#大于100个用户
        return 3
    else:#正常添加用户
        bank[username]={
            "account":account,
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
        info = '''
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
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
index=int(input("请输入您的操作"))

def Deposit():
    DA = int(input("请输入存钱的账号:"))
    if DA in bank:
        savemoney = int(input("存款金额:"))
        bank[DA]["money"] += savemoney
    else:
        print("请确认存款账号是否正确!")
# def  add():
#     a=int(input("数字"))
#     b=int(input("数字2"))
#     c=a+b
#     if c==10:
#         return 1
# if add(5,5) ==1:
#     print("成功")