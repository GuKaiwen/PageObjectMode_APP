from Basic.base import Base
from selenium.webdriver.common.by import By
import Page


# 继承Base类
class Search_Page(Base):

    #重写父类__init__方法
    def __init__(self, driver):
        Base.__init__(self, driver)

    def search_page(self, text):
        #点击输入框
        self.click_element(Page.S_B)
        #输入框输入
        self.input_value(Page.S_B, text)
        #点击返回按钮
        self.click_element(Page.S_R)

