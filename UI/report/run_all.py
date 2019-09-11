import HTMLTestRunner
import unittest
casePath = "C:\\Users\\suyu9\\PycharmProjects\\UI\\case"
rule = "text*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
filepath = "C:\\Users\\suyu9\\PycharmProjects\\UI\\report\\htmlreport1.html"
fp = open(filepath, 'wb')


runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is first report')
runner.run(discover)
fp.close