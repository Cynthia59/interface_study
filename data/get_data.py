from util.operation_excel import OperationExcel
from . import data_config
from util.operation_json import OperationJson
class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #是否携带header
    def is_header(self, row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    #获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_request_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    #获取url
    def get_url(self, row):
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    #获取请求数据
    def get_data(self, row):
        col = int(data_config.get_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    #通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        data = opera_json.get_data_by_key(self.get_data(row))
        return data

    #获取预期数据
    def get_expect(self, row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    #写入数据
    def write_result(self, row, value):
        col = int(data_config.get_result())
        self.opera_excel.write_value(row, col, value)

    #获取依赖数据的key
    def get_depend_key(self, row):
        col = int(data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == '':
            return None
        else:
            return depend_key

if __name__ == '__main__':
    gd = GetData()
    print(gd.get_case_lines())