import unittest

#使用unittest框架编写测试用例
from hc_api_study_0610.common.hc_req_api import HcApi


class Test_Zhuti(unittest.TestCase):
    def setUpClass(cls):#表示在类之前执行

    def tearDownClass(cls):

    def test_get_zhuti(self,testcase_title,tesecase_num):
        self._testMethodDoc = testcase_title
        self._testMethodName = tesecase_num
        res = HcApi().get_zhuti_api()
