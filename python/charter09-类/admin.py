from user import User
# 管理员 :管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。
# 添加一个名为privileges 的属性，用 于存储一个由字符串(如"can add post" 、"can delete post" 、"can ban user" 等)组成的列表。
# 编写一个名为show_privileges() 的方法，它 显示管理员的权限。创建一个Admin 实例，并调用这个方法
class Admin(User):
    def __init__(self,first_name, last_name, privileges, **propertys):
        super(Admin, self).__init__(first_name, last_name, **propertys)
        self.privileges = Privileges(privileges)
    def show_privileges(self):
        self.privileges.show_privileges()

# 管理员 :管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。
# 添加一个名为privileges 的属性，用 于存储一个由字符串(如"can add post" 、"can delete post" 、"can ban user" 等)组成的列表。
# 编写一个名为show_privileges() 的方法，它 显示管理员的权限。创建一个Admin 实例，并调用这个方法
class Admin(User):
    def __init__(self,first_name, last_name, privileges, **propertys):
        super(Admin, self).__init__(first_name, last_name, **propertys)
        self.privileges = Privileges(privileges)
    def show_privileges(self):
        self.privileges.show_privileges()

# 权限 :编写一个名为Privileges 的类，它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。
# 将方法show_privileges() 移到这 个类中。在Admin 类中，将一个Privileges 实例用作其属性。
# 创建一个Admin 实例，并使用方法show_privileges() 来显示其权限
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print(self.privileges)

