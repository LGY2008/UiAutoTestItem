"""以下为项目 url地址"""
# 自媒体url
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理
url_mis = "http://ttmis.research.itcast.cn/#/"

# app 包名启动名
appPackage = "com.itcast.toutiaoApp"
appActivity = ".MainActivity"

"""以下为自媒体登录配置数据 """
from selenium.webdriver.common.by import By
# 手机号
mp_phone = By.CSS_SELECTOR, ".el-input__inner"
# 验证码
mp_verify_code = By.CSS_SELECTOR, "[placeholder='验证码']"
# 登录按钮
mp_login_btn = By.CSS_SELECTOR, ".el-button--primary"
# 昵称
mp_nickname = By.CSS_SELECTOR, ".user-name"
# 内容管理
mp_content_manage = By.XPATH, "//*[text()='内容管理']"
# 发布文章
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 标题
mp_title = By.XPATH, "//*[@placeholder='文章名称']"
# iframe 查找iframe元素，根据元素切换iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 内容
mp_content = By.CSS_SELECTOR, "#tinymce"
# 点击 封面->自动
mp_cover = By.XPATH, "//*[text()='自动']"
# 点击 频道
mp_channel = By.XPATH, "//*[@placeholder='请选择']"
# 具体频道
mp_channel_detail= By.XPATH, "//*[text()='数据库']"
# 点击 发布
mp_send = By.CSS_SELECTOR, ".el-button.filter-item.el-button--primary"
# 获取发布文章结果
mp_result = By.XPATH, "//*[contains(text(),'成功')]"

"""以下数据为 后台管理系统配置数据"""
# 用户名
mis_username = By.CSS_SELECTOR, "[name='username']"
# 密码
mis_pwd = By.CSS_SELECTOR, "[name='password']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, "#inp1"
# 昵称
mis_nickname = By.CSS_SELECTOR, ".user_info>span"
# 信息管理
mis_info_manage = By.XPATH, "//*[contains(text(),'信息管理')]"
# 内容审核
mis_content_audit = By.XPATH, "//*[contains(text(),'内容审核')]"
# 文章名称
mis_title = By.XPATH, "//*[@placeholder='请输入: 文章名称']"
# 输入 频道
mis_channel = By.XPATH, "//*[@placeholder='请输入: 频道']"
# 选择 审核状态
mis_select_status = By.XPATH, "//*[@placeholder='请选择状态']"
# 具体的状态 待审核
# 点击 查询
mis_search = By.CSS_SELECTOR, ".find"
# 点击 通过
mis_pass = By.XPATH, "//div[@class='cell']//span[text()='通过']/.."
# 点击 确认通过
mis_pass_confirm= By.CSS_SELECTOR, ".el-button--primary"
# 判断是否审核通过  根据id 切换状态为审核通过
mis_article_id = By.CSS_SELECTOR, ".cell>span"

"""以下为app配置数据"""
# 手机号
app_phone = By.XPATH, "//*[@index='1' and @class='android.widget.EditText']"
# 验证码
app_code = By.XPATH, "//*[@index='2' and @class='android.widget.EditText']"
# 登录按钮
app_login_btn = By.CLASS_NAME, "android.widget.Button"
# 我的
app_me = By.XPATH, "//*[contains(@text,'我的') and @index='3']"
# 频道滚动区域
app_swipe_area = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']"
app_swipe_area_two = By.XPATH, "//*[@bounds='[0,520][1440,2288]']"