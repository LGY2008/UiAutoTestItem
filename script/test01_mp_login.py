import sys
import os

import pytest

sys.path.append(os.getcwd())
from tool.read_yaml import ReadYaml
from tool.get_log import GetLog

# 获取日志器
log = GetLog.get_log()
from time import sleep
import page
from page.page_mp_login import PageMpLogin
from tool.get_driver import GetDriver


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 获取 PageMpLogin对象
        self.login = PageMpLogin(GetDriver.get_driver(page.url_mp))

    # 结束
    def teardown_class(self):
        # 只能调用 自己封装的方法
        GetDriver.quit_driver()

    # 测试方法
    @pytest.mark.parametrize("phone,code,expect",ReadYaml("mp_login.yaml").get_data())
    def test_mp_login(self, phone, code, expect):
        # 调用登录业务方法
        self.login.page_login(phone, code)
        try:
            # 断言
            nickname = self.login.page_get_nickname()
            assert nickname == expect
            print("登录的昵称为：", nickname)
        except Exception as e:
            # 截图
            self.login.base_get_img()
            # 日志
            log.error(e)
            # 抛异常
            raise
