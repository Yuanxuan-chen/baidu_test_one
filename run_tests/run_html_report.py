import unittest
from HTMLTestRunner import HTMLTestRunner

# 批量导入测试用例
test_dir = '../test_case'
suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')

# 运行器
runner = unittest.TextTestRunner()
runner.run(suite)