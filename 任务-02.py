# 一、有一个列表，[“北京”,”上海”,”广东”]
# (1)将中国所有省会城市添加到上述列表中
# (2)广东成为第二大发达城市，将广东排在上海前面
# (3)[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
#    这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
# #(1)将中国所有省会城市添加到上述列表中
# provincial_capital = ["北京","上海","广东"]  # 省会城市列表
# while True:
#     city = input("请输入省会城市,输入结束,结束操作！:")
#     if city == "结束":
#         break
#     provincial_capital.append(city)
# for i in range(len(provincial_capital)):
#     print(provincial_capital[i])

# #(2)广东成为第二大发达城市，将广东排在上海前面
# city = ["北京","上海","广东"]
# temp = city[1]
# city[1] = city[2]
# city[2] = temp
# for i in range(len(city)):
#     pr = city[i]
#     print(pr)

# #(3)[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# #    这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
# gdp = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# total_GDP = 0
# for i in range(len(gdp)):
#     total_GDP += gdp[i]
# print("前8城市的GDP总和:",total_GDP)
# average_GDP=total_GDP / 8
# print("平均GDP:",average_GDP)

# #二、有以下一个列表，求其中是5的倍数的和。a = [1,5,21,30,15,9,30,24]
# a = [1,5,21,30,15,9,30,24]
# Sum = 0
# for i in range(len(a)):
#     if a[i]%5==0:
#         Sum += a[i]
# print("5的倍数的和:",Sum)

# #三、有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）
# # List = [1,2,3,4,5,6,7,8,9]
# # 实现效果：list = [9,8,7,6,5,4,3,2,1]
# List = [1,2,3,4,5,6,7,8,9]
# list = []
# # subscript = 8
# List.reverse()
# for i in range(len(List)):
#      list.append(List[i])
# print("list = ",list)

# #四、请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# for i in range(len(List)):
#     count = 0
#     frequency = 0
#     while count < len(List):
#         if List[i] == List[count]:
#             frequency += 1
#         count +=1
#     print(List[i],"出现次数:",frequency)