
import unittestreport
import unittest
from DXWeb.testCases.test_dxweb import TestDXWeb
#用例套件
suite = unittest.TestSuite()
#用例加载器
loader = unittest.TestLoader()
cases = loader.loadTestsFromTestCase(TestDXWeb)
#添加用例
suite.addTests(cases)
print('用例数：',suite.countTestCases())

unittestreport.TestRunner(suite,
                 filename="report.html",
                 report_dir="./reports",
                 title='测试报告',
                 tester='测试员',
                 desc="XX项目测试生成的报告",
                 templates=2
                 ).run()


