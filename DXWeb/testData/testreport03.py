
import unittestreport
import unittest

#用例套件
suite = unittest.TestSuite()
#用例加载器
testcases  = unittest.defaultTestLoader.discover(r'D:\test\pythonMw\DXWeb\testCases',pattern='test*.py')

#添加用例
suite.addTests(testcases)
print(suite.countTestCases())

unittestreport.TestRunner(suite,
                 filename="report1.html",
                 report_dir="./reports",
                 title='测试报告',
                 tester='测试员',
                 desc="XX项目测试生成的报告",
                 templates=2
                 ).run()


