import unittest
from page_test.test_search_page import TestSearchPage

# 测试套件
suite = unittest.TestSuite()
suite.addTest(TestSearchPage('test_click_logo'))

# 运行器
runner = unittest.TextTestRunner()
runner.run(suite)
