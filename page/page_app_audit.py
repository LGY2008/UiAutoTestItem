from time import sleep

import page
from base.base_app import BaseApp


class PageAppAudit(BaseApp):
    # 查找频道
    def page_search_channel(self, channel):
        sleep(2)
        self.base_right_swipe_left(page.app_swipe_area, channel)

    # 查找文章
    def page_search_article(self, title_text):
        # self.base_down_swipe_up(title_text)

        # 限制区域
        self.base_dow_swipe_up_two(page.app_swipe_area_two, title_text)
    # 查找文章业务方法
    def page_article(self, channel, title_text):
        self.page_search_channel(channel)
        self.page_search_article(title_text)