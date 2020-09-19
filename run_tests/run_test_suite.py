import unittest
from test_case.test_search_page import TestSearchPage

# 测试套件
suite = unittest.TestSuite()

# 添加测试用例
# 方法一
# suite.addTest(TestSearchPage('test_click_logo'))
# suite.addTests(TestSearchPage('test_search_page'))

# 方法二
# cases = [TestSearchPage('test_click_logo'), TestSearchPage('test_search_page')]
# suite.addTests(cases)

# 方法三, 批量导入测试用例
test_dir = '../'
discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')

# 运行器
runner = unittest.TextTestRunner()
runner.run(discover)
