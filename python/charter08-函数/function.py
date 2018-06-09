# 定义函数
def greet_user():
    print("hello")
greet_user()


# 消息 :编写一个名为display_message() 的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message():
    print("I was learning python")
display_message()

# 编写一个名为favorite_book() 的函数，其中包含一个名为title 的形参。这个函数打印一条消息，如One of my favorite books is
# Alice in Wonderland 。调用这个函数，并将一本图书的名称作为实参传递给它。

def favorite_book(title):
    print("one of my favorite books is "+title)

favorite_book("平凡的世界")

# 位置实参
def describe_pet(animal_type, pet_name): #"""显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')

# 关键字实参

describe_pet(pet_name='harry', animal_type='hamster')

# 形参默认值
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

# T恤 :编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数应打印一个句子，概要地说明T恤的尺码和字样。 使用位置实参调用这个函数来制作一件T恤;再使用关键字实参来调用这个函数
def make_shirt(size, words):
    print("the shirt size is "+size+ ", the words is "+words)
make_shirt("25cm", 'it is my world')
make_shirt(size='36cm', words='hello world')

# 大号T恤 :修改函数make_shirt() ，
# 使其在默认情况下制作一件印有字样“I love Python”的大号T恤。
# 调用这个函数来制作如下T恤:一件印有默认字样的大号T 恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤(尺码无关紧要)
def make_shirt(size, words="I love Python"):
    print("the shirt size is "+size+ ", the words is "+words)
make_shirt("大号")
make_shirt("中号")
make_shirt("unknow",words="othe worlds")

# 城市 :编写一个名为describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。
# 这个函数应打印一个简单的句子，如Reykjavik is in Iceland 。
# 给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家
def describe_city(name, country):
    print(name+" is in "+country)
describe_city("beijing", 'china')
describe_city("paris", 'franch')
describe_city("taiwan", 'china')

# 返回字典
def build_person(first_name, last_name):
     person = {'first': first_name, 'last': last_name}
     return person
musician = build_person('jimi', 'hendrix')
print(musician)

# 城市名 :编写一个名为city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串
# "Santiago Chile"

def city_country(city,country):
    return city+" "+country
str = city_country("shanghai", "china")
print(str)

str = city_country("new york", "america")
print(str)

str = city_country("man gu", "taiguo")
print(str)

# 专辑 :编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使
# 用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给函数make_album() 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个 函数，并至少在一次调用中指定专辑包含的歌曲数
def make_album(singer, album, songnum=0):
    detail = {"singer":singer, "album":album}
    if songnum > 0:
        detail['songnum'] = songnum
    return detail
detail = make_album("jay zhou", 'qi li xiang')
print(detail)

detail = make_album("JJ", 'caocao', 5)
print(detail)

# 用户的专辑 :在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函 数make_album() ，并将创建的字典打印出来。
# 在这个while 循环中，务必要提供退出途径
# while True:
#     singer = input("please input the singer name:")
#     album = input("please input the album name:")
#     print(make_album(singer, album))
#     repeat = input("repeat the input ,yes or no?")
#     if repeat == "no" or repeat !='yes':
#         break

# 修改列表
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians() 的函数，这个函数打印列表中每个魔术师的名字
def show_magicians(magicians):
    print("the magicians names list is:")
    for magician in magicians:
        print(magician)
magicians = ['davaid', 'jmesyan', 'liuqian']
show_magicians(magicians)

# 了不起的魔术师 :在你为完成练习8-9而编写的程序中，编写一个名为make_great() 的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the
# Great”。调用函数show_magicians() ，确认魔术师列表确实变了
def make_great(ma)