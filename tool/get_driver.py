import page
from selenium import webdriver
import appium.webdriver


class GetDriver:
    # web driver变量
    driver = None
    # app driver变量
    driver_app = None

    # 获取driver
    @classmethod
    def get_driver(cls, url):
        if cls.driver is None:
            # 获取 浏览器对象
            cls.driver = webdriver.Chrome()
            # 最大化
            cls.driver.maximize_window()
            # 打开 url
            cls.driver.get(url)
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须置空
            cls.driver = None


    # 获取app应用driver
    @classmethod
    def get_driver_app(cls):
        if cls.driver_app is None:
            # server 启动参数
            desired_caps = {}
            # 设备信息
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'CSX0217728000025'
            # app的信息 /
            desired_caps['appPackage'] = page.appPackage
            desired_caps['appActivity'] = page.appActivity
            # 中文
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 不重置应用
            desired_caps['noReset'] = False
            # 声明我们的driver对象
            cls.driver_app = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls.driver_app

    @classmethod
    def quit_driver_app(cls):
        if cls.driver_app:
            cls.driver_app.quit()
