from selenium.webdriver.support.ui import WebDriverWait

class Base(object):

    def __init__(self, driver):
        self.driver = driver

        # desired_caps = {}
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # def find_element(self, loc, loc_value, timeout=10, poll=0.5):
    #     """
    #     :param loc: 定位方式
    #     :param loc_value:
    #     :return:
    #     """
    #     return WebDriverWait(self.driver, timeout, poll)\
    #         .until(lambda x: x.find_element(loc, loc_value))

    def find_element(self, loc, timeout=10, poll=0.5):
        """
        :param loc: 元组，参数格式（定位方式，”属性值“）
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll)\
            .until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        self.find_element(loc).click()

    def input_value(self, loc, value):
        """
        :param loc: 元组
        :param value:
        :return:
        """
        self.find_element(loc).send_keys(value)


