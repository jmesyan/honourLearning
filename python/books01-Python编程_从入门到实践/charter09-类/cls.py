#coding=utf-8
from restaurant import Restaurant
from admin import Admin,User
from collections import OrderedDict
from random import randint
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+ " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")


my_dog.sit()
my_dog.roll_over()

# 餐馆 :创建一个名为Restaurant 的类，其方法__init__() 设置两个属性:restaurant_name 和cuisine_type 。
# 创建一个名 为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业
#根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法


restaurant = Restaurant("my_result", "good")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 三家餐馆 :根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
res1 = Restaurant("a", "b")
res2 = Restaurant("c", "d")
res3 = Restaurant("e", "f")
res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()

# 就餐人数 :在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant 的实 例;打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它

restaurant = Restaurant('hewolf', "ade")
print(restaurant.number_serverd)
restaurant.number_serverd  = 5
print(restaurant.number_serverd)

# 添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值
restaurant.set_number_serverd(21)
print(restaurant.number_serverd)

# 添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值:你认为这家餐馆每天可能接待的就
# 餐人数。

restaurant.increment_number_serverd(8)
print(restaurant.number_serverd)



user1 = User("jmes", "yan", age=23)
user1.describe_user()
user1.greet_user("nice to meet you")

# 尝试登录次数 :在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。
# 编写一个名为increment_login_attempts() 的方法， 它将属性login_attempts 的值加1。
# 再编写一个名为reset_login_attempts() 的方法，它将属性login_attempts 的值重置为0。
# 根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。打印属性login_attempts 的值，确认它被正确地递增;
# 然后，调用方 法reset_login_attempts() ，并再次打印属性login_attempts 的值，确认它被重置为0。
user2 = User("lucky", "dvaid", age = 18)
user2.increment_login_attemps()
print(user2.login_attempts)
user2.reset_login_attempts()
print(user2.login_attempts)

#类的继承
class Car():
# class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
             print("You can't roll back an odometer!")
    def increment_odometer(self, miles): self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar, self).__init__(make, model, year)
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 冰淇淋小店 :冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant 类。
# 这两个版 本的Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋 的方法。创建一个IceCreamStand 实例，并调用这个方法。

class IceCreamStand(Restaurant):
      def __init__(self, restaurant_name, cuisine_type, iceCream, number_serverd=0):
          super(IceCreamStand, self).__init__(restaurant_name, cuisine_type, number_serverd)
          self.flavors = iceCream
      def describe_iceCreams(self):
          for ice in self.flavors:
              print(ice)

iceRestaurant = IceCreamStand("icci", "lucky", ['good', 'orange'],2)
iceRestaurant.describe_restaurant()
iceRestaurant.describe_iceCreams()
iceRestaurant.increment_number_serverd(3)
print(iceRestaurant.number_serverd)


# admin = Admin("lisha","yan",["can add post", "cadd delet post"],aget=13)
# admin.describe_user()
# admin.show_privileges()



admin = Admin("lisha","yan",["can add post", "cadd delet post"],aget=13)
admin.describe_user()
admin.show_privileges()

# 导入Restaurant 类 :将最新的Restaurant 类存储在一个模块中。
# 在另一个文件中，导入Restaurant 类，创建一个Restaurant 实例，并调 用Restaurant 的一个方法，以确认import 语句正确无误


# 导入Admin 类 :以为完成练习9-8而做的工作为基础，
# 将User 、Privileges 和Admin 类存储在一个模块中，再创建一个文件，
# 在其中创建一个Admin 实例 并对其调用方法show_privileges() ，以确认一切都能正确地运行

# 多个模块 :将User 类存储在一个模块中，并将Privileges 和Admin 类存储在另一个模块中。
# 再创建一个文件，在其中创建一个Admin 实例，并对其调用方 法show_privileges() ，以确认一切都依然能够正确地运行

#使用python 标准库

favorite_languages = OrderedDict()
# favorite_languages = {}
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

#骰子 :模块random 包含以各种方式生成随机数的函数，其中的randint() 返回一个位于指定范围内的整数，例如，下面的代码返回一个1~6内的整数
# from random import randint
# x = randint(1, 6)
# 请创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。编写一个名为roll_die() 的方法，它打印位于1和骰子面数之间的随机数。
# 创建一个6面 的骰子，再掷10次。 创建一个10面的骰子和一个20面的骰子，并将它们都掷10次

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        x = randint(1, self.sides)
        print(x)
    def roll_test(self, nums):
            num = 0
            while (num < nums):
                 num+=1
                 self.roll_die()
print("6 sizes:")
die1 = Die()
die1.roll_test(10)
print("10 sizes:")
die1 = Die(10)
die1.roll_test(10)
print("20 sizes:")
die1 = Die(20)
die1.roll_test(10)

# Python Module of the Week :要了解Python标准库，一个很不错的资源是网站Python Module of the Week。请访问http://pymotw.com/ 并查看其中的目录，在其中找一
# 个你感兴趣的模块进行探索，或阅读模块collections 和random 的文档。









