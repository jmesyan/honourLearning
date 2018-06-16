class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_serverd=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = number_serverd

    def describe_restaurant(self):
        print("the restaurant_name is:"+self.restaurant_name+" and the cuisine_type is:"+self.cuisine_type)

    def open_restaurant(self):
        print("the restaurant is working")
    def set_number_serverd(self, num):
        self.number_serverd = num
    def increment_number_serverd(self, num):
        self.number_serverd+=num