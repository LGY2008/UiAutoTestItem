import page
from base.base import Base


class PageMisLogin(Base):
    # 输入 用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 输入 密码
    def page_input_pwd(self, pwd):
        self.base_input(page.mis_pwd, pwd)

    # 点击 登录
    def page_click_login_btn(self):
        # 处理元素的 disabled 属性值
        js = "document.getElementById('inp1').disabled = false"
        # 调用执行js方法
        self.driver.execute_script(js)
        self.base_click(page.mis_login_btn)

    # 获取 昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 登录业务方法
    def page_mis_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 登录业务方法
    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()