# -*- coding: utf_8 -*-
import unittest
import time
from HttpLibrary import HttpApi
import HTMLTestRunner
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
#
class TestApi(unittest.TestCase):
    def setUp(self):
        self.api = HttpApi()


    def test_QueryExpress(self):
        '''查询快递单'''
        url = "http://www.kuaidi100.com/query"
        data = {'type': 'jd', 'postid': '121212'}
        result = self.api.http_request("GET", url, data, False)
        if result == None:
            self.assertTrue(False)
        else:
            self.assertEqual(result['status'], u'201')
            self.assertEqual(result['message'], u'快递公司参数异常：单号不存在或者已经过期')


def Suite():
    testunit = unittest.TestSuite()
    testunit.addTest(TestApi("test_QueryExpress"))
    return testunit


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HtmlFile = "/usr/local/test/" + now + "HTMLtemplate.html"
    #HtmlFile= "D:/pythoncharm/apitest/" + now + "HTMLtemplate.html"
    print("123")
    fp = file(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试提交", description=u"用例测试执行情况")
    runner.run(Suite())