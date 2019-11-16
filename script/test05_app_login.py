import sys
import os

sys.path.append(os.getcwd())
from tool.get_log import GetLog
from time import sleep

from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


class TestAppLogin:
    # 初始化
    def setup_class(self):
        # 获取dirver
        driver = GetDriver.get_driver_app()
        # 获取PageAppLogin对象
        self.login = PageIn(driver).page_get_pageAppLogin()

    # 结束
    def teardown_class(self):
        # 关闭drive
        sleep(10)
        GetDriver.quit_driver_app()

    # 登录测试方法
    def test_app_login(self, phone="13012345678", code="246810"):
        # 调用业务方法
        self.login.page_login(phone, code)
        try:
            print("是否登录成功：", self.login.page_is_login_success())
            # 断言
            assert self.login.page_is_login_success()
        except Exception as e:
            # 截图
            self.login.base_get_img()
            # 日志
            log.error(e)
            # 抛异常
            raise
