# #一、实现输入10个数字，并打印10个数的求和结果
# count = 1
# sum1 = 0
# while count < 11:
#     print("请输入",count,"个数字:")
#     number = int(input())
#     sum1 += number
#     count +=1
# print("10个数的和：",sum1)

##二、从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# Max = 0
# sum = 0
# average = 0
# count = 1
# while count <=10:
#     print("请输入第",count,"个数字：")
#     number = int(input())
#     sum += number
#     if number > Max:
#         temp = number
#         Max = temp
#     count +=1
# average = sum / 10
# print("最大数：",Max)
# print("10个数的总和：",sum)
# print("和平均数：",average)

# #三、使用random模块，如何产生 50~150之间的数？
# import random
# random_number = random.randint(50,150)
# print("随机数:",random_number)

# #四、从键盘输入任意三边，判断是否能形成三角形，若可以，
# # 则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# side1 = int(input("请输入第一条边："))
# side2 = int(input("请输入第二条边："))
# side3 = int(input("请输入第三条边："))
# if (side1 + side2 > side3) and (side1 + side3 >side2) and (side2 + side3 > side1):
#     print("能形成三角形")
#     if(side1 == side2 ==side3):
#         print("等边三角形")
#     elif (side1 == side2) or (side1 == side3) or (side2 == side3):
#         print("等腰三角形")
#     elif (side1 * side1) + (side2 * side2) == (side3 *side3):
#         print("直角三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不能形成三角形")

# #五、有以下两个数，使用+，-号实现两个数的调换。A=56、B=78,A=78、B=56
# A = 56
# B = 78
# A = A + B
# B = A - B
# A = A - B
# print("A=",A)
# print("B=",B)

# #六、实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# user_name = "root"
# password = "admin"
# for i in range(3):
#     user_name1 = input("请输入用户名：")
#     password1 = input("请输入密码：")
#     if user_name1 == user_name and password1 == password:
#         print("登录成功！")
#         break
#     else:
#         print("登录失败，请重试！")

# #七、编程实现下列图形的打印
# count1 =1
# while count1 <= 7:
#     count2 = 1
#     while count2 < 8-count1:
#         print(" ",end="")
#         count2 +=1
#     count3 = 1
#     while count3 <= count1:
#         print("*",end=" ")
#         count3 +=1
#     print()
#     count1 +=1

# #八、1使用while循环实现99乘法表的打印。(正序)
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         product = i * j
#         print(j,"*",i,"=",product,end="  ")
#         j +=1
#     print()
#     i+=1

# #八、2编程实现99乘法表的倒叙打印
# i = 9
# while i >= 1:
#     j = 1
#     while j <= i:
#         product = i * j
#         print(j,"X",i,"=",product,end=" ")
#         j +=1
#     print()
#     i-=1

# # #九、一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# i = 0
# b = 3
# h = 2
# t = 0
#
# while True:
#     i += b
#     t += 1
#     if i == 20:
#         break
#     i -= h
#     if i == 20:
#         break
# print("第",t,"天出来")

##十、用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
##第一种方法：
# Sum = 1
# for i in range(1,21):# i= 1,
#     j = i # j= 1,
#     while j >=i:#到二结束
#         Sum *= i
#         j -=1
# print(Sum)
#
# #第二种方法：
# class Factorial:
#     def fact(self,num):
#         if num > 0:
#             return num*self.fact(num-1)
#         else:
#             return 1
#
# num = float(input('输入要求的阶乘:'))
# a = Factorial()
# ret = a.fact(num)
# print(ret)