# 该实例演示了数字猜谜游戏
number = 89
guess = -1
print("数字猜谜游戏！")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    
    if guess == number:
        print("恭喜你猜对了！")
    elif guess < number:
        print("猜的数字小了哦")
    elif guess > number:
        print("猜的数字大了哦") 