from appium import webdriver


def init_driver():
    # 服务端启动参数
    desired_caps = {}
    # 手机 系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    # 设备号
    desired_caps['deviceName'] = 'ERLDU20421006535'
    # 包名
    desired_caps['appPackage'] = 'com.android.settings'
    # 启动名
    desired_caps['appActivity'] = '.HWSettings'
    # 允许输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    return driver