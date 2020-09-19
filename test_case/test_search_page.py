import unittest
from ddt import ddt, data
from selenium import webdriver

from page_object.search_page import *


# 搜索页面的测试用例
@ddt
class TestSearchPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.sp = SearchPage(webdriver.Chrome())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.sp.close()

    def setUp(self) -> None:
        self.sp.open(SearchPage.baidu_url)

    @data('666', '123', '562')
    def test_search_page(self, txt):
        """测试搜索框的功能"""
        self.sp.search_input(txt)
        self.sp.search_button()

    def test_click_logo(self):
        """点击搜索框上面的logo"""
        self.sp.click_logo()


if __name__ == '__main__':
    unittest.main()
