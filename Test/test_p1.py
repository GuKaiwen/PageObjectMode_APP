import sys, os
sys.path.append(os.getcwd())

from Basic.base import Base
from appium import webdriver
from selenium.webdriver.common.by import By

class Test_AddUser:

    def setup_class(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        # 版本
        desired_caps['platformVersion'] = '9'
        # 设备名称
        desired_caps['deviceName'] = 'ERLDU20421006535'
        # app信息
        # 包名
        desired_caps['appPackage'] = 'com.android.settings'
        # 启动名
        desired_caps['appActivity'] = '.HWSettings'
        # 申明手机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.base_driver = Base(self.driver)

    def test_001(self):
        #搜索框
        S_B = (By.ID, "android:id/search_src_text")
        #返回按钮
        S_R = (By.ID, "com.android.settings:id/back")
        #点击搜索框
        self.base_driver.click_element(S_B)
        #输入数字123
        self.base_driver.input_value(S_B,123)
        #点击返回按钮
        # self.base_driver.click_element(S_R)
        self.base_driver.find_element(S_R).click()

    def teardown_class(self):
        self.driver.quit()