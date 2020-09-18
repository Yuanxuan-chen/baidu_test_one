import unittest
from page_test.test_search_page import TestSearchPage

# 测试套件
suite = unittest.TestSuite()

# 添加测试用例
# 方法一
suite.addTest(TestSearchPage('test_click_logo'))
# suite.addTests(TestSearchPage('test_search_page'))

# 方法二
# cases = [TestSearchPage('test_click_logo'), TestSearchPage('test_search_page')]
# suite.addTests(cases)

# 运行器
runner = unittest.TextTestRunner()
runner.run(suite)
