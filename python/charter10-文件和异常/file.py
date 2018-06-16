#从文件中读出数据
with open("pi_digits.txt") as file_object:
     contents = file_object.read()
     print(contents.rstrip())

# 逐行读取
with open("pi_digits.txt") as file_object:
    for line in file_object:
        print(line)


# 创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# 使用文件的内容
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

# Python学习笔记 :在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，
# 其中每一行都以“In Python you can”打头。将这个文件命名为 learning_python.txt，
# 并将其存储到为完成本章练习而编写的程序所在的目录中。
# 编写一个程序，它读取这个文件，并将你所写的内容打印三次:
# 第一次打印时读取整个 文件;第二次打印时遍历文件对象;
# 第三次打印时将各行存储在一个列表中，再在with 代码块外打印它们
with open("learning_python.txt") as file:
        # contents = file.read()
        # print(contents.rstrip())
        # for line in file:
        #     print(line)
        lines = file.readlines()
for line in lines:
    print(line)

# C语言学习笔记 :可使用方法replace() 将字符串中的特定单词都替换为另一个单词。下面是一个简单的示例，演示了如何将句子中的'dog' 替换为'cat'
# >>> message = "I really like dogs." >>> message.replace('dog', 'cat') 'I really like cats.
# 读取你刚创建的文件learning_python.txt中的每一行，将其中的Python都替换为另一门语言的名称，如C。将修改后的各行都打印到屏幕上

with open("learning_python.txt") as file:
    contents = file.read()
    print(contents.replace("Python", "C"))

# 写入空文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# 写入多行
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 附加到文件 -使用模式-“a”
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# 访客 :编写一个程序，提示用户输入其名字;用户作出响应后，将其名字写入到文件guest.txt中
# username = input("请输入你的用户名")
# filename = "guest.txt"
# with open(filename, "a") as file_object:
#     file_object.write(username+"\n")

#访客名单 :编写一个while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。
# 确保这个文件中的每条记录都独占一行。
# filename = "guest_book.txt"
# while(True):
#     username = input("请输入你的姓名")
#     if username == "quit":
#         break
#     print("Hello "+ username)
#     with open(filename, "a") as file_object:
#         file_object.write(username+"\n")

# 关于编程的调查 :编写一个while 循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
# while True:
#     reason = input("你为何喜欢编程")
#     if reason == "quit" : break
#     with open("q.txt", "a") as file_object:
#         file_object.write(reason+"\n")








