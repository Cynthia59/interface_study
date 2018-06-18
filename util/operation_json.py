import json

class OperationJson():
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = '../dataconfig/login.json'
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open(self.file_name) as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data_by_key(self, key):
        return self.data[key]

if __name__ == '__main__':
    j = OperationJson()
    print(j.data)
    print(j.get_data_by_key('login'))
