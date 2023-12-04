from Page.search import Search_Page

"""
公共入口
"""
class Page_Obj(object):
    def __init__(self, driver):
        self.driver = driver

    def Search_Page_Obj(self):
        return Search_Page(self.driver)