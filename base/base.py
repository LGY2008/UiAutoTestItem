from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tool.get_log import GetLog

# 获取日志器
log = GetLog.get_log()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info("正在获取driver对象::{}".format(driver))
        self.driver = driver

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素：{} ，超时时间: {}, 查找的频率: {}".format(loc, timeout, poll))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 查找一组元素
    def base_finds(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素：{} ，超时时间: {}, 查找的频率: {}".format(loc, timeout, poll))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_elements(*loc))

    # 输入
    def base_input(self, loc, value):
        log.info("正在调用输入方法：")
        # 获取元素
        el = self.base_find(loc)
        # 清空
        log.info("正在对：{} 元素执行清空操作".format(loc))
        el.clear()
        # 输入
        log.info("正在对：{} 元素执行输入: {} 操作".format(loc, value))
        el.send_keys(value)

    # 点击
    def base_click(self, loc):
        log.info("正在对：{}元素，执行点击操作".format(loc))
        self.base_find(loc).click()

    # 获取 文本方法
    def base_get_text(self, loc):
        text = self.base_find(loc).text
        log.info("正在对：{}元素，执行获取文本操作，获取的文本内容为：{}".format(loc, text))
        return text

    # 截图
    def base_get_img(self):
        log.info("正在对执行截图操作")
        self.driver.get_screenshot_as_file("./image/err.png")
        self.base_write_img_report()

    # 将图片写入测试报告
    def base_write_img_report(self):
        log.info("正在将图片写入allure报告")
        with open("./image/err.png", "rb") as f:
            allure.attach("失败原因：", f.read(), allure.attach_type.PNG)

    # 下拉框 选择
    def base_click_li(self, placeholder_text, click_text):
        # 点击 下拉框
        loc = By.XPATH, "//*[contains(@placeholder,'{}')]".format(placeholder_text)
        self.base_click(loc)
        sleep(1)
        # 点击 具体状态
        loc = By.CSS_SELECTOR, "ul>li"
        els = self.base_finds(loc)
        for el in els:
            if el.text == click_text:
                el.click()
                break

    # 判断元素是否存在
    def base_element_is_exists(self, el_text):
        loc = By.XPATH, "//*[contains(text(), '{}')]".format(el_text)
        try:
            self.base_find(loc, timeout=3)
            print("找到了！")
            return True
        except:
            print("未找到！")
            return False
