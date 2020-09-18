from selenium.webdriver.common.by import By

from base.base import *


class SearchPage(Base):
    """百度搜索页面, driver: 引入webdriver"""
    baidu_url = "https://www.baidu.com/"

    def search_input(self, txt):
        """搜索框, txt: 搜索内容"""
        self.locator((By.XPATH, "//input[@id = 'kw']")).send_keys(txt)

    def search_button(self):
        """搜索按钮"""
        self.locator((By.XPATH, "//input[@id = 'su']")).click()

    def click_logo(self):
        """点击搜索框上面的logo"""
        self.locator((By.XPATH, '//*[@id="lg"]/map/area')).click()

