from time import sleep

import page
from base.base import Base


class PageMpArticle(Base):
    # 点击 内容管理
    def page_click_content_manage(self):
        self.base_click(page.mp_content_manage)

    # 点击 发布文章
    def page_click_publish_article(self):
        self.base_click(page.mp_publish_article)

    # 输入 标题
    def page_input_title(self, title):
        self.base_input(page.mp_title, title)

    # 输入 内容
    def page_input_content(self, content):
        # 切换iframe
        el = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(el)
        # 输入内容
        self.base_input(page.mp_content, content)
        # 回到默认目录
        self.driver.switch_to.default_content()

    # 点击 封面->自动
    def page_click_cover_auto(self):
        self.base_click(page.mp_cover)

    # 点击 频道
    def page_click_channel(self):
        # 点击频道选择框
        self.base_click(page.mp_channel)
        sleep(1)
        # 点击具体频道
        self.base_click(page.mp_channel_detail)

    # 点击发布按钮
    def page_click_send_btn(self):
        self.base_click(page.mp_send)

    # 获取新增结果
    def page_get_article_result(self):
        return self.base_get_text(page.mp_result)

    # 组合发布文章业务方法
    def page_article(self,title, content):
        sleep(2)
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        sleep(1)
        self.page_input_content(content)
        self.page_click_cover_auto()
        self.page_click_channel()
        self.page_click_send_btn()
