#coding=utf-8

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#访问第二个元素

print(bicycles[1])

# 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来
names = ["lucy", 'davide']
print(names[0])
print(names[1])

# 而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名
msg = " good morning"
print(names[0].title()+msg)
print(names[1].title()+msg)

# 修改列表元素
names[0]= "jmesyan"
print(names)

# 末尾添加元素
names.append("xiaoliang")
print(names)

# 插入列表元素
names.insert(0, "lili")
print(names)

# 删除names第一个元素
del names[1]
print(names)

# 删除POP
name = names.pop()
print(name)
print(names)

# Popr任意元素
name = names.pop(0)
print(name)
print(names)

names.append("abd")
names.append("def")
print(names)

# 根据值删除元素
names.remove("abd")
print(names)

# 如果你可以邀请任何人一起共进晚餐(无论是在世的还是故去的)，你会邀请哪些人?请创建一个列表，其中包含至少3个你想邀请的人;然后，使用 这个列表打印消息，邀请这些人来与你共进晚餐
names.append("heipi")
print(names)
print(names[0]+",would your like to have dinner with us")

# 你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。 再次打印一系列消息，向名单中的每位嘉宾发出邀请
print(names[1]+" can't  take part");
names[1] = "lucy"
print(names)

# 你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。 以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。 使用insert() 将一位新嘉宾添加到名单开头。
# 使用insert() 将另一位新嘉宾添加到名单中间。
# 使用append() 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀

print("we find a big table");
names.insert(0, "jmsyan")
print(names)

names.insert(2, "kaite")
print(names)

names.append("zhuanjia1")
print(names)

print(names[0]+", it is my pleasure to invite you to my big table")


# 你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。 以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进 晚餐。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
print("We just take a message, the new table can't delivery in time, we cant only invite two guests")
name1 = names.pop(0);
print(name1+", i am sorry to tell you we cancel the party");
print(names[3]+" and "+ names[4]+", welcome to take  our party")
del names[3]
del names[3]
print(names)

# 使用sort进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#使用sorted临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(sorted(cars,reverse=True))
print(cars)

#reverse反转队列
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#确定列表长度
print(len(cars))

# 想出至少5个你渴望去旅游的地方。 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。 使用sorted() 按字母顺序打印这个列表，同时不要修改它。 再次打印该列表，核实排列顺序未变。
# 使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。 再次打印该列表，核实排列顺序未变。
# 使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
# 使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。 使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
# 使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了

tours = ['lijiang', 'huangshan', 'newyouk', 'mardf']
print(sorted(tours))
print(tours)
print(sorted(tours, reverse=True))
print(tours)
tours.reverse()
print(tours)
tours.reverse()
print(tours)
tours.sort()
print(tours)
tours.sort(reverse=True)
print(tours)