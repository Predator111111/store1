import pymysql

# #数据库学习与实践
# import pymysql
# #链接数据库
# con = pymysql.connect(host="localhost",user="root",passwd="",database="中国工商银行")
# #创建控制台
# cursor = con.cursor()
# #创建SQL语句
# # sql = "insert into article value('s006','手机','3500','50')"
# sql = ""
# #控制台执行SQL语句
# cursor.execute(sql)
# #提交到数据库
# con.commit()
# #关闭资源
# cursor.close()
# con.close()
host = "localhost"
user="root"
password=""
database="中国工商银行"


#定义增、删、改方法
#parameter1 = SQL语句, parameter2 = 增、删、改的条件
def modify(parameter1,parameter2):
    #链接数据库
    linkm = pymysql.connect(host=host,user=user,passwd=password,database=database)
    #创建控制台
    cursor=linkm.cursor()
    #创建SQL语句,并执行语句
    cursor.execute(parameter1,parameter2)
    # 执行语句后提交数据
    linkm.commit()
    #关闭资源
    cursor.close()
    linkm.close()
#定义查询方法
#parameter1 = SQL语句,parameter2 = 查询的约束条件
# parameter3 = 查询条件,parameter4 = 查询条数
def query(parameter1,parameter2,parameter3 = "all",parameter4 = 1):
    #链接数据库
    linkq = pymysql.connect(host=host,user=user,passwd=password,database=database)
    #创建控制台
    cursor=linkq.cursor()
    #创建SQL语句，并执行语句
    cursor.execute(parameter1,parameter2)
    #控制台输出提示
    # print(
    #     "查询一条数据：请输入one","\n",
    #     "查询全部数据：请输入all","\n",
    #     "查询自定义：请输入many"
    # )
    #判断查询条件
    if parameter3 == "all":
        return cursor.fetchall()
    elif parameter3 == "one":
        return cursor.fetchone()
    elif parameter3 == "many":
        return cursor.fetchmany(parameter4)
    else:
        print("输入非法，请重新输入！")
    #语句执行后的数据提交到数据库
    linkq.commit()
    #关闭资源
    cursor.close()
    linkq.close()









