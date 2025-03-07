a = 100
sum = 0
counter = 1
while counter <= a:
    sum = sum + counter
    counter += 1
print("1到 %d 的和为：%d" % (a,sum))

count = 0
while count < 5:
    print(count,"小于5")
    count += 1
else:
    print(count,"大于或等于5")

sites = ["Baidu","Google","Runoob","Taobao"]
for site in sites:
    if site == "Google":
        print("Google 找到了")
        break
    print("循环数据"+site)
else:
    print("没有循环数据")
print("完成循环")

word = 'python'
for letter in word:
    print(letter)

for number in range(10,20):
    print(number)

for i in range(len(sites)):
    print(i,sites[i])

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)

for letter in 'python':
    if letter == 'h':
        break
    print("当前字母：",letter)

for num in range(0,10):
    if num % 2 == 0:
        continue
    print(num)

for m in range(2,100):
    for n in range(2,m):
        if m % n == 0:
            print(m,'等于',n,'*',m//n)
            break
    else:
        print(m,'是一个质数')

class MyEmptyClass:
    pass

for y in 'runoob':
    if y == 'o':
        pass
        print("执行pass块")
    print("当前字母：",y)
print('Good Bye!')

#外边一层循环控制行数
#i是行数
i = 1
while i <= 9:
     #里面一层循环控制每一行中的列数
     j = 1
     while j<=i:
          mut =j*i
          print("%d*%d=%d"%(j,i,mut), end="  ")
          j+=1
     print("")
     i+=1
