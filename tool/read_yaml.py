import yaml

class ReadYaml:
    def __init__(self, filename):
        self.filename = filename

    def read_yaml(self):
        with open("./data/"+self.filename,"r", encoding="utf-8")as f:
            return yaml.load(f)

    def get_data(self):
        arr = []
        for data in self.read_yaml().values():
            arr.append(tuple(data.values()))
        return arr



if __name__ == '__main__':
    # print(read_yaml("mp_article.yaml"))
    # """预期结果：[(),()]"""
    #
    # print("--" * 50)
    # 创建新列表 追加读取出来的数据，组装格式为列表格式
    # arr = []
    # for data in read_yaml("mp_login.yaml").values():
    #     arr.append((data.get("phone"),data.get("code"),data.get("expect")))
    # print(arr)
    # print("--" * 50)

    """第二种方法"""
    # arr = []
    # for data in read_yaml("mp_login.yaml").values():
    #     arr.append(tuple(data.values()))
    # print(arr)


    """发布文章"""
    # arr = []
    # for data in read_yaml("mp_article.yaml").values():
    #     arr.append(tuple(data.values()))
    # print(arr)


    print(ReadYaml("mp_article.yaml").get_data())