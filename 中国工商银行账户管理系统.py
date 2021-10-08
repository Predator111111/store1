import random
from Database_tools import *

#系统提示信息
def interface():
    print("==============================================")
    print("|------------中国工商银行账户管理系统------------|")
    print("|------------1、开户              ------------|")
    print("|------------2、存钱              ------------|")
    print("|------------3、取钱              ------------|")
    print("|------------4、转账              ------------|")
    print("|------------5、查询              ------------|")
    print("|------------6、退出              ------------|")
    print("==============================================")


# 定义开户函数
def add_user():
    #添加信息
    account_number = random.randint(10000000, 99999999)
    user_name = input("请输入用户名：")
    password = int(input("请输入密码："))
    print("下面请输入你的地址：")
    country = input("\t\t请输入所在的国家：")
    province = input("\t\t请输入所在的省份：")
    street = input("\t\t请输入所在的街道：")
    house_number = input("\t\t请输入门牌号：")
    bank_name = input("请输入银行名称：")
    # 账户余额
    money = 0
    #准备SQL语句
    sql_add1 = "select count(*) from b_user"
    par1 = []
    data1 = query(sql_add1,par1)#((100))
    sql_add2 = "select * from b_user where username = %s"
    par2 = [user_name]
    data2 = query(sql_add2,par2)
    #查询结果进行判断
    if data1[0][0] > 100:
        print("数据库内存已满")
        return 3

    elif len(data2) != 0:
        print("用户名已存在")
        return 2
    else:
        sql_add3 = "insert into b_user values (%s,%s,%s,%s,%s,%s,%s,%s,now(),%s) "
        par3 = [account_number, user_name, password, country, province, street, house_number, money, bank_name]
        modify(sql_add3, par3)

        #打印个人信息
        print("恭喜你，开户成功，开户信息如下：")
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
        print(info % (
        user_name, account_number, country, province, street, house_number, money,
        bank_name))
        return 1


# 定义存钱函数
# paremeter1 = 用户的账号,parameter2 = 存取的金额
def save_money(parameter1, parameter2):
    #定义SQL查找语句
    sql_save1 = "select * from b_user where account = %s"
    par1 = [parameter1]
    data = query(sql_save1,par1)
    #执行查询语句后，进行结果判断
    if data[0][0] == parameter1:
        sql_save2 = "update b_user set money = money + %s where account = %s "
        par2 = [parameter2,parameter1]
        modify(sql_save2,par2)
        #打印存款凭证
        info = '''
                    ------------存款凭证------------
                            用户名:%s
                            银行账号：%s
                            存入金额：%s
                            开户行名称：%s

                '''
        print(info % (data[0][1],data[0][0], parameter2,data[0][9]))
        return True
    else:
        return False


# 定义取钱函数
# parameter1 用户的账号 parameter2 用户密码 parameter3 取钱金额
def withdraw_money(parameter1, parameter2, parameter3):
    #查询用户账号
    sql_withdraw1 = "select * from b_user where account = %s"
    par1 = [parameter1]
    data1 = query(sql_withdraw1,par1)
    #查询后进行判断
    if data1[0][0] == parameter1:
        if data1[0][2] == parameter2:
            sql_withdraw2 = "update b_user set money = money - %s where account = %s "
            par2 = [parameter3,parameter1]
            modify(sql_withdraw2,par2)
            #打印取款凭证
            info = '''
                                ------------取款凭证------------
                                        用户名:%s
                                        银行账号：%s
                                        取款金额：%s
                                        开户行名称：%s

                            '''
            print(info % (data1[0][1], data1[0][0], parameter3, data1[0][9]))
            return 3
        else:
            return 2
    else:
        return 1

# 定义转账函数
# parameter1 转出的账号,parameter2 转入的账号,parameter3 转出账户的密码,
# parameter4 转出的金额

def transfer_accounts(parameter1, parameter2, parameter3, parameter4):
    #查询转出账号
    sql_transfer1 = "select * from b_user where account = %s "
    par1 = [parameter1]
    data1 = query(sql_transfer1,par1)
    #查询转入账号
    sql_transfer2 = "select * from b_user where account = %s "
    par2 = [parameter2]
    data2 = query(sql_transfer2,par2)
    if data1[0][0] == parameter1 and data2[0][0] == parameter2:
        if data1[0][0] == parameter1 and data1[0][2] == parameter3:
            if data1[0][7] > parameter4:
                #修改转出账户的金额
                sql_transfer3 = "update b_user set money = money - %s where account = %s"
                par3 = [parameter4,parameter1]
                modify(sql_transfer3,par3)
                #修改转入账户的金额
                sql_transfer4 = "update b_user set money = money + %s where account = %s"
                par4 = [parameter4,parameter2]
                modify(sql_transfer4,par4)
                #打印转账凭证
                info = '''
                                                    ------------转账凭证------------
                                                            转出账号:%s
                                                            转入账号：%s
                                                            转出账号密码：******
                                                            转出金额：%s
                                                            转入金额：%s
                                                            开户行名称：%s

                                                '''
                print(info % (parameter1, parameter2, parameter4, parameter4, data1[0][9]))

            else:
                return 3
        else:
            return 2
    else:
        return 1


#定义查询账函数
#parameter1 账号,parameter2 账号密码
def query_account(parameter1,parameter2):
    #查询账号
    sql_query1 = "select * from b_user where account = %s"
    par1 = [parameter1]
    data1 = query(sql_query1,par1)
    if data1[0][0] == parameter1:
        if data1[0][2] == parameter2:
            #打印个人信息
            info = '''
                                    ------------个人信息------------
                                            当前账号:%s
                                            密码：%s
                                            余额：%s元
                                            国家：%s
                                            省份：%s
                                            街道：%s
                                            门牌号：%s
                                            开户行名称：%s
                                '''
            # 每个元素都可传入%
            print(info % (
                data1[0][0], data1[0][2], data1[0][7], data1[0][3],
                data1[0][4], data1[0][5], data1[0][6],data1[0][9]))
        else:
            print("密码不正确！")
    else:
        print("该用户已存在！")


# 业务选择
while True:
    interface()
    choice = input("请选择业务：")
    if choice == "1":
        print()
        result1 = add_user()
        print(result1)
    elif choice == "2":
        print("存钱")
        account_number2 = int(input("请输入银行卡账号："))
        monetary_limit = int(input("请输入存钱的金额："))
        result2 = save_money(account_number2,monetary_limit)
        print(result2)
    elif choice == "3":
        print("取钱")
        account_number3 = int(input("请输入账号："))
        password3 = int(input("请输入密码："))
        withdrawal_amount3 = int(input("请输入取款金额："))
        result3 = withdraw_money(account_number3,password3,withdrawal_amount3)
        print(result3)
    elif choice == "4":
        print("转账")
        transfer_out_account4 = int(input("请输入转出的账号："))
        transfer_to_account4 = int(input("请输入转入的账号："))
        transfer_out_password4 = int(input("请输入转出的密码："))
        transfer_out_amount4 = int(input("请输入转出金额："))
        result4 = transfer_accounts(transfer_out_account4,transfer_to_account4,
                                    transfer_out_password4,transfer_out_amount4)
        print(result4)

    elif choice == "5":
        print("查询")
        account_number5 = int(input("请输入账号："))
        user_password5 = int(input("请输入用户密码："))
        query_account(account_number5,user_password5)
    elif choice == "6":
        print("退出系统")
        break
    else:
        print("输入非法！")
        break


