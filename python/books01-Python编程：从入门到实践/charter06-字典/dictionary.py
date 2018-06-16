#coding:utf-8

#简单定义
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name 、last_name 、age 和city 。将存储在该字典中 的每项信息都打印出来
friend_li = {'first_name':'yan', 'last_name':'ming', 'age':'28', 'city':'beijing'}
for pro in friend_li:
    print(pro+" is:"+ friend_li[pro])

# 使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中的键;
# 想出每个人喜欢的一个数字，并将这些数字作为值存 储在字典中。打印每个人的名字和喜欢的数字。
# 为让这个程序更有趣，通过询问朋友确保数据是真实的
favorite_nums = {'xiaoliang':'11', 'xiaoxiang':'12', 'wangshuai':'13', 'jmesyan':'16'}
for friend in favorite_nums:
    print(friend+" like the num:"+favorite_nums[friend])


#Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
#  想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# 以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义;
# 也可在一行打印词汇，再使用换行符(\n )插 入一个空行，然后在下一行以缩进的方式打印词汇的含义
words = {'list':'列表', 'str':'字符串', 'int':'整数', 'float':'浮点数', 'if':'if判断语句'}
for word in words:
    print("\t"+word +" :"+words[word])


# 既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其中的一系列print 语句替换为一个遍历字典中的键和值的循环。
# 确定该 循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中
for word, explains in words.items():
    print("" + word + " :" + explains)

# 创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt' 。
# 使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
# 使用循环将该字典中每条河流的名字都打印出来。
# 使用循环将该字典包含的每个国家的名字都打印出来
rivers = {'huanghe':'china','changjiang':'china', 'nile':'egypt'}
for river, country in rivers.items():
    print("The "+river+" runs through "+ country)
for river in rivers.keys():
    print("the river name is:"+river)
for country in set(rivers.values()):
    print("the river country is:"+ country)

#在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。
# 对于还未参与调查的人，打印一条消息邀请他参与调查

mumbers = ['user1', 'user2', 'user3']
searchs = {'user1':'c++', 'user3':'php'}
for smem in mumbers:
    if smem in searchs.keys() :
        print(smem+" thank you ")
    else:
        print(smem+" welcome to help us")

# 在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people 的列表中。遍历这个列表，将其中每个人的所有 信息都打印出来

friend_0 = {'first_name':'yan', 'last_name':'ming', 'age':'28', 'city':'beijing'}
friend_1 = {'first_name':'xiao', 'last_name':'ling', 'age':'28', 'city':'beijing'}
friend_2 = {'first_name':'guo', 'last_name':'rui', 'age':'28', 'city':'hangzhou'}
people = [friend_0, friend_1, friend_2]

for friend in people:
    for k, v in friend.items():
        print(k+ " is :" + v)

# 创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名;在每个字典中，包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为pets 的列表中，再遍历该列表，并将宠物的所有信息都打印出来
pets_1 = {"lucy":{'type':'cat', 'owner':'liling'}}
pets_2 = {"dvaid":{'type':'dog', 'owner':'jmeyan'}}
pets_3 = {"link":{'type':'snake', 'owner':'niucah'}}
pets = [pets_1, pets_2, pets_3]
for pet in pets:
    for k, v in pet.items():
        print(k+" is a "+ v['type']+", and it is owner is "+v['owner'])

# 创建一个名为favorite_places 的字典。在这个字典中，将三个人的名字用作键;
# 对于其中的每个人，都存储他喜欢的1~3个地方。
# 为让这个练 习更有趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来
favorite_places = {
    "lucy":['hangzhou', 'shanghai', 'beijing'],
    'lily':['lijiang', 'guagnzhou']
}

for name, places in favorite_places.items():
    print(name+" like those places:")
    for place in places:
        print(place)

#修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来
favorite_nums = {'xiaoliang':[11, 12], 'xiaoxiang':[12,13], 'wangshuai':[13,14], 'jmesyan':[15,16]}
for name, nums in favorite_nums.items():
    print(name+" like those nums")
    for num in nums:
        print(num)

# 创建一个名为cities 的字典，其中将三个城市名用作键;对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该
# 城市的事实。在表示每座城市的字典中，应包含country 、population 和fact 等键。将每座城市的名字以及有关它们的信息都打印出来
citys = {
    "beijing":{
        'county':'china',
        'population':'300milion',
        'fact':'the air is dirty'
    },

    "new york":{
        'county':'america',
        'population':'200milion',
        'fact':'good'
    }
}

for city, intro in citys.items():
    print(city+ "'s county is "+ intro['county']+", population is "+ intro['population']+ " and the fact "+ intro['fact'])