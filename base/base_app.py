from selenium.webdriver.common.by import By

from base.base import Base


class BaseApp(Base):
    # 判断元素是否存在
    def base_app_element_is_exists(self, loc):
        try:
            self.base_find(loc, timeout=4)
            return True
        except:
            return False

    # 从右向左滑
    def base_right_swipe_left(self, area_loc, channel_text):
        # 获取区域元素
        el = self.base_find(area_loc)
        # 获取元素 大小
        width = el.size.get("width")
        height = el.size.get("height")
        print("width:", width)
        print("height:", height)
        # 获取元素 位置
        x = el.location.get("x")
        y = el.location.get("y")
        print("x:", x)
        print("y:", y)
        # 计算 start_x，start_y, end_x,end_y
        start_x = x + width * 0.8
        start_y = y + height * 0.5
        end_x = x + width * 0.2
        end_y = y + height * 0.5

        # 定义 查找文本的loc
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(channel_text)
        # 获取当前页面结构
        page_source = self.driver.page_source
        # 循环
        while True:
            try:
                # 查找元素 ->注意修改时间
                el = self.base_find(loc, timeout=2)
                print("找到了！位于屏幕的坐标：{}".format(el.location))
                # 点击
                el.click()
                # 结束 break
                break
            except:
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=3000)
                print("执行滑动屏幕操作！")
            # if 判断当前页面结构 是否等于 滑动之前 页面结构（判断是否滑动到最右侧）
            if page_source == self.driver.page_source:
                print("没找到，划不动啦！")
            else:
                # 更新 page_source 此处为一个等号，因为是赋值， 不是判断
                page_source = self.driver.page_source

    # def base_down_swipe_up(self, title_text):
    #     # 获取屏幕 大小
    #     width = self.driver.get_window_size().get("width")
    #     height = self.driver.get_window_size().get("height")
    #     print("width:", width)
    #     print("height:", height)
    #
    #     # 计算 start_x，start_y, end_x,end_y
    #     start_x = width * 0.5
    #     start_y = height * 0.8
    #     end_x = width * 0.5
    #     end_y = height * 0.2
    #
    #     # 定义 查找文本的loc
    #     loc = By.XPATH, "//*[contains(@text,'{}')]".format(title_text)
    #     # 获取当前页面结构
    #     page_source = self.driver.page_source
    #     # 循环
    #     while True:
    #         try:
    #             # 查找元素 ->注意修改时间
    #             el = self.base_find(loc, timeout=2)
    #             print("找到了！位于屏幕的坐标：{}".format(el.location))
    #             print("找到的内容为：", el.text)
    #             # 点击
    #             el.click()
    #             # 结束 break
    #             break
    #         except:
    #             # 滑动屏幕
    #             self.driver.swipe(start_x, start_y, end_x, end_y, duration=3000)
    #             print("执行滑动屏幕操作！")
    #         # if 判断当前页面结构 是否等于 滑动之前 页面结构（判断是否滑动到最右侧）
    #         if page_source == self.driver.page_source:
    #             print("没找到，划不动啦！")
    #         else:
    #             # 更新 page_source 此处为一个等号，因为是赋值， 不是判断
    #             page_source = self.driver.page_source


    # 从右向左滑
    def base_dow_swipe_up_two(self, area_loc, title_text):
        # 获取区域元素
        el = self.base_find(area_loc)
        # 获取元素 大小
        width = el.size.get("width")
        height = el.size.get("height")
        print("width:", width)
        print("height:", height)
        # 计算 start_x，start_y, end_x,end_y
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2

        # 定义 查找文本的loc
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(title_text)
        # 获取当前页面结构
        page_source = self.driver.page_source
        # 循环
        while True:
            try:
                # 查找元素 ->注意修改时间
                el = self.base_find(loc, timeout=2)
                print("找到了！位于屏幕的坐标：{}".format(el.location))
                # 点击
                el.click()
                # 结束 break
                break
            except:
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=3000)
                print("执行滑动屏幕操作！")
            # if 判断当前页面结构 是否等于 滑动之前 页面结构（判断是否滑动到最右侧）
            if page_source == self.driver.page_source:
                print("没找到，划不动啦！")
            else:
                # 更新 page_source 此处为一个等号，因为是赋值， 不是判断
                page_source = self.driver.page_source