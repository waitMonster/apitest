# -*- coding:utf-8 -*-
# 编码注释，解决中文报错问题

# 引入requests模块 库，该库是第三方专门用于处理Http请求的
import requests
# 引入python日志模块
import logging
# 引入时间处理模块
import time


class HttpApi():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler(
            str(time.strftime('%Y%m%d%H%M', time.localtime(time.time()))) + 'http_autotest_interface.log')
        self.fmt = '%(asctime)s:%(message)s'
        self.formatter = logging.Formatter(self.fmt)
        self.handler.setFormatter(self.formatter)
        self.handler.setLevel(logging.INFO)
        self.logger.addHandler(self.handler)
        self.hdr = logging.StreamHandler()
        self.formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
        self.hdr.setFormatter(self.formatter)
        self.logger.addHandler(self.hdr)



    def get_url(self):
        return self.url

    def get_data(self):
        return self.data

    def set_login_url(self, url):
        self.login_url = url

    def get_login_url(self):
        return self.login_url

    def set_login_data(self, data):
        self.login_data = data

    def get_login_data(self):
        return self.login_data

    def http_request(self, type, url, data, isCookie):
        self.url = url
        self.data = data
        if type == 'POST':
            # 定制请求头信息
            headers = {'user-agent': 'application/json'}
            if isCookie:
                conn = self.get_cookie_result(self.login_url, self.login_data)
                try:
                    result = conn.post(self.url, self.data, headers=headers)
                    self.logger.info(result.text)
                    return result.json()
                except:
                    return None
            else:
                try:
                    result = requests.post(self.url, self.data, headers=headers)
                    self.logger.info(result.text)
                    return result.json()
                except:
                    return None
        elif type == 'GET':
            try:
                result = requests.get(self.url, params=self.data)
                self.logger.info(result.text)
                # python中内置了JSON解码器，帮助你处理返回的JSON结果
                return result.json()
            except:
                return None



    def get_cookie_result(self, login_url, login_data):
        self.login_url = login_url
        self.login_data = login_data
        conn = requests.session()
        result = conn.post(login_url, login_data)
        self.logger.info(result.text)
        return conn


if __name__ == '__main__':
    # 被测接口url地址
    url = "http://www.4snow.cn/Home/Index/go/op/updatepwd"
    # 被测接口请求参数
    data = {'password': '123456', 'newpwd': '123456'}
    apitest = HttpApi()
    apitest.set_login_url("http://www.4snow.cn/Home/Index/go/op/login")
    re = apitest.http_request('POST', url,data,True)

