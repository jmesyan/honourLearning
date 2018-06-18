#coding:utf-8

# 编写一系列条件测试;将每个测试以及你对其结果的预测和实际结果都打印出来。你编写的代码应类似于下面这样:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 你并非只能创建10个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到conditional_tests.py中。对于下面列出的各种测
# 试，至少编写一个结果为True 和False 的测试。

# 检查两个字符串相等和不等。
# 使用函数lower() 的测试。 检查两个数字相等、不等、大于、小于、大于等于和小于等于。
# 使用关键字and 和or 的测试。
# 测试特定的值是否包含在列表中。
# 测试特定的值是否未包含在列表中

str1  = "Nany"
str2 = "nany"
print("Is Nany == nany?")
print(str1 == str2)
print(str1.lower() == str2)

print("the num compare")
num1 = 4
num2 = 5
print(num1 < num2)
print(num1 <= num2)
print(num1 > num2)

print("the multi conditon compare")
print(str1 != str2 and num1 < num2)
print(str1 == str2 or num1 > num2)

print("the list in or not in compare")
list = ['l1', 'l2']
print('l2' in list)
print('l3' in list)

# 外星人颜色#1 :假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green' 、'yellow' 或'red' 。
# 编写一条if 语句，检查外星人是否是绿色的;如果是，就打印一条消息，指出玩家获得了5个点。
#  编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过(未通过测试时没有输出）
alien_color = "green"
if alien_color == "green":
    print("you get 5 coin")
alien_color = "yellow"
if alien_color != "green":
    print("you lose 5 coin")

# 外星人颜色#2 :像练习5-3那样设置外星人的颜色，并编写一个if-else 结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
#  如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
#  编写这个程序的两个版本，在一个版本中执行if 代码块，而在另一个版本中执行else 代码块
if alien_color == "grren":
    print("kill the alien you get five point")
else:
    print("you get 10 point")

# 外星人颜色#3 :将练习5-4中的if-else 结构改为if-elif-else 结构。
#  如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
#  如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
# 编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息

if alien_color == "green":
    print(5)
elif alien_color == "yellow":
    print(10)
elif alien_color == "red":
    print(15)

#人生的不同阶段 :设置变量age 的值，再编写一个if-elif-else 结构，根据age 的值判断处于人生的哪个阶段。
#  如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
#  如果一个人的年龄为2(含)~4岁，就打印一条消息，指出他正蹒跚学步。
# 如果一个人的年龄为4(含)~13岁，就打印一条消息，指出他是儿童。
# 如果一个人的年龄为13(含)~20岁，就打印一条消息，指出他是青少年。
# 如果一个人的年龄为20(含)~65岁，就打印一条消息，指出他是成年人。
# 如果一个人的年龄超过65(含)岁，就打印一条消息，指出他是老年人
age  = 28
if  age < 2:
    print("he is a baby")
elif age >=2 and age <4:
    print("he is learning walk")
elif age >=4 and age < 13:
    print("he is a child")
elif age>=13 and age <20:
    print("he is a young man")
elif age>=20 and age < 65:
    print("he is a audlt")
else:
    print("he is a old man")

# 喜欢的水果 :创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if 语句，检查列表中是否包含特定的水果。 将该列表命名为favorite_fruits ，并在其中包含三种水果。
# 编写5条if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!”

favorite_fruits = ['orange', 'apple', 'banana']
if 'banana' in favorite_fruits:
    print("You really like bananas!")

# 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

# 特殊方式跟管理员打招呼 :创建一个至少包含5个用户名的列表，且其中一个用户名为'admin' 。想象你要编写代码，在每位用户登录网站后都打印一条问 候消息。遍历用户名列表，并向每位用户打印一条问候消息。
# 如果用户名为'admin' ，就打印一条特殊的问候消息，如“Hello admin, would you like to see a status report?”。
# 否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again
users = ['admin', 'user1', 'user2', 'user3']
for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello '+user+', thank you for logging in again')

# 处理没有用户的情形 :在为完成练习5-8编写的程序中，添加一条if 语句，检查用户名列表是否为空。
# 如果为空，就打印消息“We need to find some users!”。
users = []
if users:
    print("we have users")
else:
    print("we need to find some users")

#检查用户名 :按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
# 创建一个至少包含5个用户名的列表，并将其命名为current_users 。
# 再创建一个包含5个用户名的列表，将其命名为new_users ，并确保其中有一两个用户名也包含在列表current_users 中。
# 遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名;否则，打印一条消息，指 出这个用户名未被使用。
# 确保比较时不区分大消息;换句话说，如果用户名'John' 已被使用，应拒绝用户名'JOHN'
current_users = ['user1', 'user2', 'user3', 'user4']
new_users = ['User1', 'user2', 'user5', 'user6']
for user in new_users:
    if user.lower() in current_users:
        print("the name "+user+" is used,please use other")
    else:
        print("the name "+user+" is not used")

# 序数 :序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
# 在一个列表中存储数字1~9。 遍历这个列表。
# 在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输出内容应为1st 、2nd 、3rd 、4th 、5th 、6th 、7th 、8th 和9th ，但每个序 数都独占一行

list = [value for value in range(1, 10)]
print(list)
for ls in list:
    if ls == 1:
        print("1st")
    elif ls == 2:
        print(str(ls)+"nd")
    elif ls == 3:
        print(str(ls)+"rd")
    else:
        print(str(ls)+"th")
