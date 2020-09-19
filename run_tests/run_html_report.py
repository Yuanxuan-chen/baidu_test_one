import unittest
from HTMLTestRunner import HTMLTestRunner

# 批量导入测试用例
test_dir = '../test_case'
suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')

# 运行器
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 生成html测试报告
fp = open("../test_report/first_report.html", "wb")
runner = HTMLTestRunner(stream=fp, title="first_report", description="试一试: first_report")
runner.run(suite)
fp.close()