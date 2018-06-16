# 处理ZeroDivisionError 异常
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")


# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else: print(answer)

# 处理FileNotFoundError 异常
# filename = 'alice.txt'
# with open(filename) as f_obj:
#     contents = f_obj.read()

# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#         msg = "Sorry, the file " + filename + " does not exist."
#         print(msg)

# 加法运算 :提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。
# 在这种情况下，当你尝试将输入转换为整数时，将引 发TypeError 异常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
# 在用户输入的任何一个值不是数字时都捕获TypeError 异常，并打印一条友好的错误消息。对你编写的程序进行测试:先输入两个数字，再输入一些文本而不是数字。

# try:
#     num1 = int(input("请输入第一个数字\n"))
#     num2 = int(input("请输入第二个数字\n"))
# except ValueError:
#     print("请输入数字")
# else:
#     print(num1+num2)

# 加法计算器 :将你为完成练习10-6而编写的代码放在一个while 循环中，让用户犯错(输入的是文本而不是数字)后能够继续输入数字
# while True:
#     try:
#         num1 = input("请输入第一个数字\n")
#         num2 = input("请输入第二个数字\n")
#         if num1 == 'q':break
#         num1 = int(num1)
#         num2 = int(num2)
#     except ValueError:
#         print("请输入数字")
#     else:
#         print(num1+num2)

# 猫和狗 :创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# 编写一个程序，尝试读取这些文件， 并将其内容打印到屏幕上。将这些代码放在一个try-except 代码块中，以便在文件不存在时捕获FileNotFound 错误，并打印一条友好的消息。
# 将其中一个文件 移到另一个地方，并确认except 代码块中的代码将正确地执行
def animals(filename):
     try:
         with open(filename) as file_object:
             contents = file_object.read()
     except FileNotFoundError:
         # print(filename+" not found")
         pass
     else:
         print(contents)
animals("cats.txt")
animals("dogs.txt")

# 沉默的猫和狗 :修改你在练习10-8中编写的except 代码块，让程序在文件不存在时一言不发

# 常见单词 :访问项目Gutenberg(http://gutenberg.org/ )，并找一些你想分析的图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
# 你可以使用方法count() 来确定特定的单词或短语在字符串中出现了多少次。例如，下面的代码计算'row' 在一个字符串中出现了多少次
# >>> line = "Row, row, row your boat" >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# 请注意，通过使用lower() 将字符串转换为小写，可捕捉要查找的单词出现的所有次数，而不管其大小写格式如何。
# 编写一个程序，它读取你在项目Gutenberg中获取的文件，并计算单词'the' 在每个文件中分别出现了多少次

with open("books.txt") as file_object:
    contents = file_object.read()
print(contents.count("the"))
print(contents.lower().count("the"))

# 使用json.dump() 和json.load()
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numebers = json.load(f_obj)
print(numbers)

# 保存和读取用户生成的数据
# filename = 'username.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")

# 重构
## 上面的重构代码
# import json
# def get_stored_username():
#     # 如果存储了用户名，就获取它""" --snip--
#     pass
# def get_new_username():
#     username = input("What is your name? ")
#     filename = 'username.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         return username
# def greet_user():
#     # """问候用户，并指出其名字"""
#     username = get_stored_username()
#     if username:
#         print("Welcome back, " + username + "!")
#     else:
#         username = get_new_username()
#         print("We'll remember you when you come back, " + username + "!")
# greet_user()

# 喜欢的数字 :编写一个程序，提示用户输入他喜欢的数字，并使用json.dump() 将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印 消息“I know your favorite number! It's _____.”
def set_favorite_num():
    num = input("输入你喜欢的数字")
    with open("favorite_nums.txt", "w") as file_object:
        json.dump(num, file_object)
def get_favorite_num():
    with open("favorite_nums.txt") as file_object:
        num = file_object.read()
        return num
# set_favorite_num()
# get_favorite_num()

# 记住喜欢的数字 :将练习10-11中的两个程序合而为一。
# 如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
# 运行这个程序两次，看看它是否像预期的那样工作。

def favorite_num():
    try:
       num = get_favorite_num()
    except FileNotFoundError:
        set_favorite_num()
    else:
        print("I know your favorite number! It's " + num)


favorite_num()
favorite_num()



