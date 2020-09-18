from time import sleep


class Base:
    """基类"""
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """打开浏览器, 网页, url"""
        self.driver.get(url)
        self.driver.maximize_window()

    def locator(self, loc):
        """定位元素"""
        return self.driver.find_element(*loc)

    def close(self):
        """关闭浏览器"""
        sleep(3)
        self.driver.quit()
