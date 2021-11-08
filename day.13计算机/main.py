'''
    1.加载所有的测试用例
    2.执行用例并生成测试报告
'''
from HTMLTestRunner import HTMLTestRunner
import unittest


# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"C:\Users\灵\PycharmProjects\pythonProject\day。13", pattern="Test*.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "测试报告",
    description="这是计算器的测试报告",
    verbosity=1,
    stream = open(file="计算器.html", mode="w+", encoding="utf-8")
)

# 3.执行用例
runner.run(tests)




# 4.任务： 使用邮件发送附件，把报告发送给我





