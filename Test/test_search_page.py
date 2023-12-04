import sys, os
sys.path.append(os.getcwd())
import pytest
from appium import webdriver
from Page.page import Page_Obj
from Basic.init_driver import init_driver
from Basic.read_data import read_data

def yaml_data():
    data_list = []
    data = read_data('data').get('Test')
    for i in data.keys():
        data_list.append(i, data.get(i).get('test'))
    return data_list

class Test_Search_Page(object):

    def setup_class(self):
        # desired_caps = {}
        # # 设备信息
        # desired_caps['platformName'] = 'Android'
        # # 版本
        # desired_caps['platformVersion'] = '9'
        # # 设备名称
        # desired_caps['deviceName'] = 'ERLDU20421006535'
        # # app信息
        # # 包名
        # desired_caps['appPackage'] = 'com.android.settings'
        # # 启动名
        # desired_caps['appActivity'] = '.HWSettings'
        # # 申明手机驱动对象
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver = init_driver()

        self.search_page_obj = Page_Obj(self.driver).Search_Page_Obj()

    # @pytest.mark.parametrize("data", [123])
    # def test_search_page(self, data):
    #     self.search_page_obj.search_page(data)

    @pytest.mark.parametrize('test_num, test', yaml_data())
    def test_search_page(self, test_num, test):
        self.search_page_obj.search_page(test)
        self.driver.get_screenshot_as_file('./screen%d.png' % test_num)

    def teardown_class(self):
        self.driver.quit()