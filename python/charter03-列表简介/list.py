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