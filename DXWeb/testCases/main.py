# import os
#
# import pytest
#
# if __name__ == '__main__':
#     '''
#         --alluredir :生成测试数据
#         ./report/result : 生成测试数据目录
#         --alluredir=./report/result :生成临时文件路径
#         test_dxweb02.py :要执行的用例文件
#     '''
#     pytest.main(["--alluredir=./report/result",'test_dxweb.py'])
#     # 命令行执行  test_allure serve allure结果文件路径
#     # 或者
#     os.system("allure generate --clean ./report/result -o ./report/html/")

import sys

print("---",sys.path)
'''
['D:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\plugins\\python-ce\\helpers\\pydev',
 'D:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\plugins\\python-ce\\helpers\\third_party\\thriftpy', 'D:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\plugins\\python-ce\\helpers\\pydev', 'D:\\Program Files\\Python3.10\\python310.zip', 'D:\\Program Files\\Python3.10\\DLLs', 'D:\\Program Files\\Python3.10\\lib', 'D:\\Program Files\\Python3.10', 'D:\\test\\pythonProject\\venv', 'D:\\test\\pythonProject\\venv\\lib\\site-packages', 'D:\\test\\pythonProject', 'D:/test/pythonProject']

'''