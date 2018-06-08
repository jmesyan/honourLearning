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