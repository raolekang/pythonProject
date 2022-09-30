import os
import unittest
from ddt import ddt, data, unpack, file_data

# 声明了ddt类装饰器
@ddt
class MyddtTest(unittest.TestCase):


    # @data方法装饰器
    # 单组元素
    @data(1,2,3)
    def test_01(self, value):   # value用来接受data的数据
        print(value)

    # 多组数据，未拆分
    @data([1,2],[3,4])
    def test_02(self, value):
        print(value)

    # 多组数据，拆分
    # @unpac拆分，相当于把数据的最外层结构去掉
    @data([5,6],[7,8])
    @unpack
    def test_03(self, value1, value2):
        print(value1, value2)

    # 单个列表字典，未拆分
    @data([{"name": "peter", "age": 15, "addr": "chengdu"}])
    def test_04(self, value):
        print(value)

    # 多个列表字典，拆分
    @data([{"name":"peter","age":16,"addr":"chengdu"},{"name":"lily","age":17,"addr":"chengdu"}])
    @unpack
    def test_05(self, value1, value2):
        print(value1, value2)

    # 单个字典，拆分
    # @data里的数据key必须与字典的key保持一致
    @data({"name":"jack","age":20})
    @unpack
    def test_06(self, name, age):
        print(name, age)

    # 多个字典, 拆分
    @data({"name":"peter","age":18,"addr":"chengdu"},{"name":"lily","age":19,"addr":"chengdu"})
    @unpack
    def test_07(self, name, age, addr):
        print(name, age, addr)

    # 多个列表字典，引用数据
    testdata = [{"name": "peter", "age": 21, "addr": "chengdu"}, {"name": "lily", "age": 22, "addr": "chengdu"}]
    @data(testdata)
    @unpack
    def test_08(self, value1, value2):
        print(value1, value2)

    # @data(*testdata)：*号意为解包，ddt会按逗号分隔，将数据拆分（不需要@unpack方法装饰器了）
    testdata = [{"name":"peter","age":23,"addr":"chengdu"},{"name":"lily","age":24,"addr":"chengdu"}]
    @data(*testdata)
    def test_09(self, value):
        print(value)

    @file_data(os.getcwd() + '/test.json')
    def test_10(self, value2):
        print(value2)


if __name__ == "__main__":
    unittest.main()