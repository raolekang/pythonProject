
import unittestreport
import unittest
from DXWeb.testCases.test_dxweb import TestDXWeb
suite = unittest.TestSuite()
suite.addTest(TestDXWeb("test_login"))
# 测试用例方法里面有别的参数，使用 testreport02.py中的方法解决
# suite.addTest(TestDXWeb("test_searchTemplate"))

unittestreport.TestRunner(suite,
                 filename="report3.html",
                 report_dir="./reports",
                 title='测试报告',
                 tester='测试员',
                 desc="XX项目测试生成的报告",
                 templates=2
                 ).run()


