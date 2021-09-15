'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
如果你的num>ran打印猜大了    <  猜小了
初始金额为500 每猜一次扣除100  如果资金为0 退出系统
如果三次没有猜中那就退出
！！！如果猜的正确的那么增加10，随机数不能只随机一次
    '''
import random
game_answer = random.randint(0,11)
monetary_limit = 500
count = 0
while count < 3:
    if monetary_limit <=0:
        print("金额不足，自动退出！")
        break
    answer = int(input("请输入你也猜的答案："))
    if answer < game_answer:
        monetary_limit -= 100
        print("猜小了，请继续")
    elif answer > game_answer:
        print("猜大了，请继续")
        monetary_limit -= 100
    else:
        print("恭喜你，猜中啦")
        monetary_limit += 100
        break
    count += 1



