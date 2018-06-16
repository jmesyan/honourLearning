# 用户 :创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。
# 在类User 中定义一个名 为describe_user() 的方法，它打印用户信息摘要;
# 再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。
#  创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User:
    def __init__(self, first_name, last_name, **propertys):
        self.propertys = {}
        self.propertys['first_name'] = first_name
        self.propertys['last_name'] =last_name
        for k, v in propertys.items():
            self.propertys[k] = v
        self.login_attempts = 0;
    def describe_user(self):
        for k,v in self.propertys.items():
            print(k+" : "+ str(v))
    def greet_user(self,msg):
        print(self.propertys['first_name']+" "+ self.propertys['last_name']+", "+msg)
    def increment_login_attemps(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts = 0