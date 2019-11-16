import logging.handlers


class GetLog:
    logger = None

    @classmethod
    def get_log(cls):
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置 日志器 总级别
            cls.logger.setLevel(logging.INFO)
            # 获取 处理器
            st = logging.handlers.TimedRotatingFileHandler(filename="./log/info.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            st_err = logging.handlers.TimedRotatingFileHandler(filename="./log/err.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 设置 处理器 级别
            st.setLevel(logging.INFO)
            st_err.setLevel(logging.ERROR)
            # 获取 格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式添加到处理器中
            st.setFormatter(fm)
            st_err.setFormatter(fm)
            # 将处理器 添加到日志器中
            cls.logger.addHandler(st)
            cls.logger.addHandler(st_err)
        # 返回 日志器->日志入口
        return cls.logger

