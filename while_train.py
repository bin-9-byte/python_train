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
    print(site)

word = 'python'
for letter in word:
    print(letter)

for number in range(10,20):
    print(number)