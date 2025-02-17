# print("this""is""string")
# word = '字符串'
# sentence = "这是一个句子。"
# paragraph = """这是一个段落，
# 可以由多行组成"""
# print(word,sentence,paragraph)

 
# input("\n\n按下 enter 键后退出。")
 
# import sys;
# sys.stdout.write(" hi " + '\n')

#!/usr/bin/python3
 
# x="a"
# y="b"
# # 换行输出
# print( x )
# print( y )
 
# print('---------')
# # 不换行输出
# print( x, end=" " )
# print( y, end=" " )
# print()

# import sys
# print('================Python import mode==========================')
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)

# import math

# result = math.sqrt(16)
# print(result)  # 输出 4.0

# from math import sqrt

# result = sqrt(16)
# print(result)  # 输出 4.0


# list = [ 1,2,3,4,5,6,7,8,9,10 ]  # 定义一个列表
# tinylist = [123, 'runoob']

# print (list)            # 打印整个列表
# print (list[0])         # 打印列表的第一个元素
# print (list[1:3])       # 打印列表第二到第四个元素（不包含第四个元素）
# print (list[2:])        # 打印列表从第三个元素开始到末尾
# print (tinylist * 2)    # 打印tinylist列表两次
# print (list + tinylist)  # 打印两个列表拼接在一起的结果

# list[0] = 100
# print(list)
# list[2:5] = [13,14,15]

# list[2:5] = []
# print(list)

#函数
# def reverseWords(input): 
      
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    # inputWords = input.split(" ") 
  
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    # inputWords=inputWords[-1::-1] 
  
    # 重新组合字符串
#     output = ' '.join(inputWords) 
      
#     return output 

# if __name__ == "__main__": 
#     input = 'I like runoob'
#     rw = reverseWords(input) 
#     print(rw)

#集合
# sites = {"google", "taobao", "runoob"}
# print(sites)
# if "runoob" in sites:
#     print("runoob在集合中")
# else:
#     print("runoob不在集合中")

# a = set('adnvdjsaife')
# b = set('lmkokoiip')
# print(a - b)#a集合中去掉b集合中的元素
# print(a | b)#a集合和b集合的并集
# print(a & b)#a集合和b集合的交集
# print(a ^ b)#a集合和b集合的差集

#!/usr/bin/python3

# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2]     = "2 - 菜鸟工具"

# tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

# print (dict['one'])       # 输出键为 'one' 的值
# print (dict[2])           # 输出键为 2 的值
# print (tinydict)          # 输出完整的字典
# print (tinydict.keys())   # 输出所有键
# print (tinydict.values()) # 输出所有值

#列表推导式
names = ['bob','tom','alice','jerry','kitty']
new_names = [name.upper()for name in names if len(name) > 3]
print(new_names)

multiples = [i for i in range(30) if i%3==0]
print(multiples)

#字典推导式
# {key_expr: value_expr for value in collection}
# {key_expr: value_expr for value in collection if condition}
list1 = ['google','taobao','bytedance','baidu']
dict1 = {key:len(key) for key in list1}
print(dict1)

dic = {x:x**2 for x in (2,4,6)}
print(dic)

#集合推导式
# {expression for item in iterable if condition}
# set1 = {i**2 for i in [1,2,3,4,5]}
# print(set1)

#[] 是用来创建列表
#() 是用来创建元组
#{} 是用来创建字典
#set() 是用来创建集合
#列表推导式
#集合推导式
#字典推导式
#b'' 是用来创建字符串 bytes() 是用来创建字节串
x = b'hello'
y = x[1:3] #切片
z = x + b'world' #拼接
print(y,z)
if x[0] == ord('h'):
    print("the first element is 'h'")
#ord() 是用来获取字符串的ASCII码
#chr() 是用来获取ASCII码对应的字符
#int(x[,base=10])
#base=10 表示十进制
#base=2 表示二进制
#base=8 表示八进制
#base=16 表示十六进制
#数据类型转换
#int() 是用来将字符串转换为整数
#float() 是用来将字符串转换为浮点数
#str() 是用来将整数转换为字符串
#list() 是用来将字符串转换为列表
#tuple() 是用来将字符串转换为元组
#set() 是用来将字符串转换为集合
#dict() 是用来将字符串转换为字典
#eval() 是用来将字符串转换为表达式
#exec() 是用来将字符串转换为代码
#compile() 是用来将字符串转换为代码对象
#repr() 是用来将字符串转换为表达式

#数据类型转换
#隐式类型转换-自动完成
#显式类型转换-需要使用类型函数来转换

# num_int = 123
# num_flo = 1.23

# num_new = num_int + num_flo

# print("num_int 数据类型为：",type(num_int))
# print("num_flo 数据类型为：",type(num_flo))
# print("num_new 值为：",num_new)
# print("num_new 数据类型为：",type(num_new))

