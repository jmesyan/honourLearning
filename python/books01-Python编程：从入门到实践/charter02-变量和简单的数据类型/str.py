#coding=utf-8

str = "the peace of love"
#第一个首字母大写
print(str.capitalize())
# 每个首字母大写
print(str.title())

#全部大写
print(str.upper())

#全部小写
print(str.lower())

#字符串拼接

str2 = " is a feeling"

str = str+str2
print(str)

#使用换行符

str = "it a interesting thing. \nbut it is boring too"
print(str)

#使用制表符

str = "\ti take a step first"

print(str)

#删除左端空白
str = str.lstrip()
print(str)


# 将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”
name = "Eric"

print("Hello " +name+", would you like to learn some Python toda")

# 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名
print(name.lower())
print(name.upper())
print(name.title())

# 名言: 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样(包括引号):
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
dictum = "A person who never made a mistake never tried anything new"
print(name+" once said, "+ dictum)
