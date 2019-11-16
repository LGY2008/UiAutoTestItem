import sys
import os

sys.path.append(os.getcwd())
from tool.get_log import GetLog
import pytest
from tool.read_yaml import ReadYaml
import page
from page.page_in import PageIn

from tool.get_driver import GetDriver

log = GetLog.get_log()


class TestMisAudit:
    # 初始化
    def setup_class(self):
        # 获取dirver
        driver = GetDriver.get_driver(page.url_mis)
        # 获取统一入口类对象
        self.pageIn = PageIn(driver)
        # 调用登录方法
        self.pageIn.page_get_pageMisLogin().page_mis_login_success()
        # 获取PageMisAudit对象
        self.audit = self.pageIn.page_get_pageMisAudit()

    # 结束
    def teardown_class(self):
        GetDriver.quit_driver()

    # 审核文章测试方法
    @pytest.mark.parametrize("title, channel, expect", ReadYaml("mis_audit.yaml").get_data())
    def test_audit_article(self, title, channel, expect):
        # 调用业务方法
        self.audit.page_audit(title, channel)
        try:
            # 判断是否成功
            result = self.audit.page_audit_is_pass(title, channel)
            print("是否审核成功：", result)
            assert result == expect
        except Exception as e:
            # 截图
            self.audit.base_get_img()
            # 日志
            log.error(e)
            # 抛异常
            raise
