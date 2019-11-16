from page.page_app_audit import PageAppAudit
from page.page_app_login import PageAppLogin
from page.page_mis_audit import PageMisAudit
from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_pageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle对象
    def page_get_pageArticle(self):
        return PageMpArticle(self.driver)

    # 获取PageMisLogin对象
    def page_get_pageMisLogin(self):
        return PageMisLogin(self.driver)

    # 获取PageMisAudit对象
    def page_get_pageMisAudit(self):
        return PageMisAudit(self.driver)

    # 获取PageAppLogin对象
    def page_get_pageAppLogin(self):
        return PageAppLogin(self.driver)

    # 获取PageAppAudit对象
    def page_get_pageAppAudit(self):
        return PageAppAudit(self.driver)