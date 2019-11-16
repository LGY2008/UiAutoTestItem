import sys
import os
sys.path.append(os.getcwd())
from tool.get_log import GetLog
from time import sleep
import pytest
from tool.read_yaml import ReadYaml

# 获取日志器
log = GetLog.get_log()
import page
from page.page_in import PageIn

from tool.get_driver import GetDriver


# def get_data():
#     arr = []
#     for data in read_yaml("mp_article.yaml").values():
#         arr.append(tuple(data.values()))
#     return arr
#

class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver(page.url_mp)
        # 获取 PageIn对象
        self.page_in = PageIn(driver)
        # 调用登录方法
        self.page_in.page_get_pageMpLogin().page_login_success()
        # 获取PageMpArticle示例对象
        self.article = self.page_in.page_get_pageArticle()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 测试方法
    @pytest.mark.parametrize("title,content,expect",ReadYaml("mp_article.yaml").get_data())
    def test_article(self, title, content, expect):
        # 调用发布文章业务方法
        self.article.page_article(title, content)
        try:
            # 断言
            assert expect == self.article.page_get_article_result()
        except Exception as e:
            # 截图
            self.article.base_get_img()
            # 日志
            log.error(e)
            # 抛异常
            raise