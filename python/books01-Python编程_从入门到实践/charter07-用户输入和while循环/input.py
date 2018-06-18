#coding:utf-8

#用户输入
# message = raw_input("Tell me something, and I will repeat it back to you: ")
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# 编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru”
# car = input("what kind of car would your like to rent?")
# print("Let me see if I can find you a "+car)

#编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌;否则指出有空桌
# nums  = input("how many people will have dinner?")
# nums = int(nums)
# if nums > 8:
#     print("there is no empty desk")
# else:
#     print("we have empty desk")

# 用户输入一个数字，并指出这个数字是否是10的整数倍。
# num = input("please input a num")
# num = int(num)
# if num % 10 == 0:
#     print("it is a num duplicat the 10")
# else :
#     print("no duplicate 10")


# 使用标志退出循环
# prompt="the active flag is:"
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# 编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨 中添加这种配
# while True:
#     message = input("add the burdening is")
#     if message =='quit':
#         break
#     else:
#         print("we will add burdening"+message+" in the pizzle")

# 有家电影院根据观众的年龄收取不同的票价:不到3岁的观众免费;3~12岁的观众为10美元;超过12岁的观众为15美元。
# 请编写一个循环，在其中询问用 户的年龄，并指出其票价
# while True:
#     age = input("input your age or quit:")
#     if age == "quit": break
#     age = int(age)
#     if age < 3:
#         print("you are free")
#     elif age >= 3 and age < 12:
#         print("the doller is 10")
#     else:
#         print("the doller is 15")


#在列表之间移动元素
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 使用用户输入来填充字典

responses = {}
# 设置一个标志，指出调查是否继续
# polling_active = True
# while polling_active: # 提示输入被调查者的名字和回答
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     # 将答卷存储在字典中
#     responses[name] = response
#     # 看看是否还有人要参与调查
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
# # 调查结束，显示结果
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")

# 熟食店 :创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名字;
# 再创建一个名为finished_sandwiches 的空列表。遍历列 表sandwich_orders ，
# 对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich ，并将其移到列表finished_sandwiches 。
# 所有三明治都制作好后，打印一条消息，将这些三明治列出来
sandwich_orders = ['a', 'b', 'c']
finished_sandwiches = []
while sandwich_orders:
     sandwich = sandwich_orders.pop()
     print("I made your "+sandwich+" sandwich")
     finished_sandwiches.append(sandwich)
print("all sandwich finished, list:")
for sandwich in finished_sandwiches:
    print(sandwich)

# 五香烟熏牛肉(pastrami)卖完了 :使用为完成练习7-8而创建的列表sandwich_orders ，并确保'pastrami' 在其中至少出现了三次。
# 在程序开头附近添加 这样的代码:打印一条消息，指出熟食店的五香烟熏牛肉卖完了;
# 再使用一个while 循环将列表sandwich_orders 中的'pastrami' 都删除。
# 确认最终的列 表finished_sandwiches 中不包含'pastrami'
sandwich_orders = ['pastrami', 'a', 'pastrami', 'b', 'pastrami', 'c']
print("the pastrami sandwich is sell over:")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")
finished_sandwiches = []
while sandwich_orders:
     sandwich = sandwich_orders.pop()
     print("I made your "+sandwich+" sandwich")
     finished_sandwiches.append(sandwich)
print("all sandwich finished, list:")
for sandwich in finished_sandwiches:
    print(sandwich)

# 梦想的度假胜地 :编写一个程序，调查用户梦想的度假胜地。
# 使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查 结果的代码块。
result = []
active = True
while active:
    place = input("If you could visit one place in the world, where would you go?")
    if place == "quit":
        active = False
    else:
        result.append(place)
print("The result is :")
for place in result:
    print(place)
