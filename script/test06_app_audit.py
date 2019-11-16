import sys
import os
from time import sleep

sys.path.append(os.getcwd())
from tool.get_log import GetLog
from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


class TestAppAudit:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver_app()
        # 获取PageIn对象
        self.pageIn = PageIn(driver)
        # 调用登录方法
        self.pageIn.page_get_pageAppLogin().page_login_success()
        # 获取PageAppAudit对象
        self.audit = self.pageIn.page_get_pageAppAudit()

    # 结束
    def teardown_class(self):
        # 关闭driver
        sleep(10)
        GetDriver.quit_driver_app()

    # 测试方法
    def test_app_audit(self, channel="python", title_text=""):
        try:
            # 调用查找文章业务方法
            self.audit.page_article(channel, title_text)
        except Exception as e:
            log.error(e)
            print(e)
