import unittest
from name_function import get_formatted_name
from city_functions import get_city
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('janis', 'joplin', "lucy")
        self.assertEqual(formatted_name, 'Janis Lucy Joplin')

# 城市和国家 :编写一个函数，它接受两个形参:一个城市名和一个国家名。这个函数返回一个格式为City, Country 的字符串，如Santiago, Chile 。
# 将 这个函数存储在一个名为city_functions.py的模块中
#创建一个名为test_cities.py的程序，对刚编写的函数进行测试(别忘了，你需要导入模块unittest 以及要测试的函数)。
# 编写一个名为test_city_country() 的 方法，核实使用类似于'santiago' 和'chile' 这样的值来调用前述函数时，得到的字符串是正确的。
# 运行test_cities.py ，确认测 试test_city_country() 通过了

class CityTestCase(unittest.TestCase):
      def test_city_country(self):
          formatted_city = get_city("Shanghai", "China")
          self.assertEqual(formatted_city, "Shanghai,China")
unittest.main()