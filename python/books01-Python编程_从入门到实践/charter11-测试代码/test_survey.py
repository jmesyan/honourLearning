import unittest
from survey import AnonymousSurvey
class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    def test_store_single_response(self):
        "测试单个答案会被妥善地存储"
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


# 雇员 :编写一个名为Employee 的类，其方法__init__() 接受名、姓和年薪，并将它们都存储在属性中。
# 编写一个名为give_raise() 的方法，它默认将 年薪增加5000美元，但也能够接受其他的年薪增加量
class Employee():
    def __init__(self, name,xing,nianxing):
         self.name = name
         self.xing = xing
         self.nianxing = int(nianxing)
    def give_raise(self, add=5000):
        self.nianxing+=add

#为Employee 编写一个测试用例，其中包含两个测试方法:test_give_default_raise() 和test_give_custom_raise() 。
# 使用方法setUp() ，以免在 每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。

class TestEmployee(unittest.TestCase):
      def setUp(self):
          self.employee = Employee("qiang","yan",0)
      def test_give_default_raise(self):
          self.employee.give_raise()
          self.assertEqual(self.employee.nianxing, 5000)
      def test_give_custom_raise(self):
          self.employee.give_raise(2000)
          self.assertEqual(self.employee.nianxing, 2000)

unittest.main()

