import page
from base.base_app import BaseApp


class PageAppLogin(BaseApp):
    # 输入 用户名
    def page_input_phone(self, phone):
        self.base_input(page.app_phone, phone)

    # 输入 验证码
    def page_input_verify_code(self, code):
        self.base_input(page.app_code, code)

    # 点击 登录按钮
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 判断是否登录成功
    def page_is_login_success(self):
        return self.base_app_element_is_exists(page.app_me)

    # 登录组合业务方法
    def page_login(self, phone, code):
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        self.page_click_login_btn()

    # 登录组合业务方法->解决依赖登录问题
    def page_login_success(self, phone="13012345678", code="246810"):
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        self.page_click_login_btn()
