import sys
import os

sys.path.append(os.getcwd())
import pytest

from tool.read_yaml import ReadYaml
import page

from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_log import GetLog

log = GetLog.get_log()


class TestMisLogin:
    # 初始化
    def setup_class(self):
        driver = GetDriver.get_driver(page.url_mis)
        # 获取PageMisLogin对象
        self.mis_login = PageIn(driver).page_get_pageMisLogin()

    # 结束
    def teardown_class(self):
        GetDriver.quit_driver()

    # 后台登录方法
    @pytest.mark.parametrize("username, pwd, expect", ReadYaml("mis_login.yaml").get_data())
    def test_mis_login(self, username, pwd, expect):
        # 调用登录业务方法
        self.mis_login.page_mis_login(username, pwd)
        try:
            # 断言 昵称
            nickname = self.mis_login.page_get_nickname()
            print("获取的昵称为：", nickname)
            assert expect in nickname
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_login.base_get_img()
            # 抛异常
            raise
