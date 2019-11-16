from time import sleep

import page
from base.base import Base


class PageMisAudit(Base):

    # 定义文章id变量
    id = None

    # 点击 信息管理
    def page_click_info_manage(self):
        self.base_click(page.mis_info_manage)

    # 点击 内容审核
    def page_click_content_audit(self):
        self.base_click(page.mis_content_audit)

    # 输入 文章名称
    def page_input_title(self, title):
        self.base_input(page.mis_title, title)

    # 输入 频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_channel, channel)

    # 选择 审核状态
    def page_click_audit(self, placeholder_text="请选择状态", click_text="待审核"):
        self.base_click_li(placeholder_text, click_text)

    # 点击 查询
    def page_click_search(self):
        self.base_click(page.mis_search)

    # 点击 通过
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass)

    # 点击 确认通过
    def page_click_confirm_pass(self):
        self.base_click(page.mis_pass_confirm)

    # 获取文章id方法
    def page_get_article_id(self):
        sleep(2)
        return self.base_get_text(page.mis_article_id)

    # 判断是否审核通过  根据id 切换状态为审核通过
    def page_audit_is_pass(self,title, channel):
        sleep(3)
        # 刷新
        self.driver.refresh()
        # 输入 文章title
        self.page_input_title(title)
        # 输入 频道
        self.page_input_channel(channel)
        # 选择 状态
        self.page_click_audit(click_text="审核通过")
        # 点击查询
        self.page_click_search()
        sleep(8)
        # 调用判断元素是否在当前页面存在
        return self.base_element_is_exists(self.id)

    # 组合业务方法
    def page_audit(self, title, channel):
        sleep(1)
        self.page_click_info_manage()
        sleep(1)
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_audit()
        self.page_click_search()
        # 获取 id 并保存
        self.id = self.page_get_article_id()
        self.page_click_pass_btn()
        sleep(2)
        self.page_click_confirm_pass()
        print("审核通过的id为：", self.id)