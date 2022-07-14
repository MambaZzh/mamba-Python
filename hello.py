import keyword as kw

print(kw.kwlist)

#  字符串定义方式 ''、""、'''、"""
str1 = "字符串1"
print(str1)

str2 = '字符串2'
print(str2)

str3 = '''
字符串3
字符串33
字符串333
'''
print(str3)

str4 = """
字符串4
字符串44
字符串444
"""
print(str)

#  转义字符\
str5 = "转义字符\n转转转"
print(str5)

#  r可以让转义字符(\)不转义
str5 = r"转义字符\n转转转"
print(str5)

x = "a"
y = "b"
print(x, end=" ")
print(y, end=" ")
print()
z = "ABCDEFG"
print(z[1:-1])
print(z[2:4])
print(z[1:3:2])

if 3 > 1:
    print("true")
    print("yes")
elif 3 > 2:
    print("ture")
else:
    print("yes or no")

x, y, z = "apple", "cherry", "banana"
a = b = c = "Hi"

def fun01():
    #  定义一个局部变量x
    x = "melon"
    print("x局部变量：" + x)


def fun02():
    #  global 关键字，声明变量为 全局变量
    global x
    x = "melon2"
    print("x全局变量：" + x)


fun01()
fun02()
print("x全局变量：" + x)

#  打印数据类型
print(type(x))

A = 10

print(type(A))

B = 1j

print(type(B))