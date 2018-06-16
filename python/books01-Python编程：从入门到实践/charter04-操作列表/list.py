#coding:utf-8

# for循环

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)

# for循环通过缩进区分块
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

# 想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for 循环将每种比萨的名称都打印出来。
# 修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。
# 在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。

pizzles = ['red', 'blue', 'orange'];
for pizzle in pizzles:
    print("I like the "+pizzle+" pizzle")
print("I really love pizza")

# 想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for 循环将每种动物的名称都打印出来。
# 修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a great pet”。
# 在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a great pet!”这样的句子

animals = ['dog', 'cat', 'pig'];
for animal in animals:
    print("A "+animal+" would make a greate pet")
print("the animals are human's friends")

#range(min,max)-生成范围内的数字

for num in range(1,5):
    print(num)

#list(range(min,max))-生成数字列表
nums = list(range(1,5))
print(nums)

# list(range(min,max, step))-指定步长生成数字列表

nums = list(range(2,11,2))
print(nums)

# 数字列表进行统计运算
print(min(nums))
print(max(nums))
print(sum(nums))

# 列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

# 使用一个for 循环打印数字1~20(含)
for num in range(1, 21):
    print(num)

# 创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来(如果输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口)
list = [value for value in range(1, 1000001)]
# for ls in list:
#     print(ls)

# 计算1~1 000 000的总和 :创建一个列表，其中包含数字1~1 000 000，再使用min() 和max() 核实该列表确实是从1开始，到1 000 000结束的。
# 另外，对这个列表 调用函数sum() ，看看Python将一百万个数字相加需要多长时间
print(min(list))
print(max(list))
print(sum(list))

#通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数;再使用一个for 循环将这些数字都打印出来。
list = [value for value in range(1,21,2)]
for ls in list:
    print(ls)

# 3的倍数 :创建一个列表，其中包含3~30内能被3整除的数字;再使用一个for 循环将这个列表中的数字都打印出来
list = [value for value in range(3,31,3)]
for ls in list:
    print(ls)

# 立方 :将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数(即1~10)的立方，再使用一个for 循 环将这些立方数都打印出来
list = [value for value in range(1,11)]
for ls in list:
    print(ls**3)

# 使用切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# 赋值列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods #这行不通-指向同一地址
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# 切片 :选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
# 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
print("The first three items in the list are:")
for ls in my_foods[:3]:
    print(ls)
print("Three items from the middle of the list are:")
for ls in my_foods[1:4]:
    print(ls)

print("The last three items in the list are:")
for ls in my_foods[-3:]:
    print(ls)

# 你的比萨和我的比萨 :在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其存储到变量friend_pizzas 中，再完成如下任务
#  在原来的比萨列表中添加一种比萨。
# 在列表friend_pizzas 中添加另一种比萨。
# 核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for 循环来打印第一个列表;打印消息“My friend's favorite pizzas are:”，再使用一
# 个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中
pizzles = ['red', 'blue', 'orange'];
friend_pizzles = pizzles[:]
pizzles.append("green")
friend_pizzles.append("yellow")
print("My favorite pizzas are:")
for ls in pizzles:
    print(ls)
print("My friend's favorite pizzas are:")
for ls in friend_pizzles:
    print(ls)

# 定义元组
dimensions = (200, 50)
print(dimensions[0])
#dimensions[0]=250 报错，元组不能重新赋值

# 遍历元组
for dimension in dimensions:
    print(dimension)

#修改元组变量 - 使用重新赋值策略
dimensions = (400, 50)
print(dimensions[0])

# 自助餐 :有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
# 使用一个for 循环将该餐馆提供的五种食品都打印出来。
# 尝试修改其中的一个元素，核实Python确实会拒绝你这样做。 餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块:给元组变量赋值，并使用一个for 循环将新元组的每个元素都打印出来
auto_foods = ('bread', 'milk', 'tomato', 'rice', 'juice')
for food in auto_foods:
    print(food)
# auto_foods[0] = "bread2"
# print(auto_foods)
auto_foods = ('bread2', 'milk2', 'tomato', 'rice', 'juice')
for food in auto_foods:
    print(food)


