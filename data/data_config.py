class global_var:
    #case_id
    Id = '0'
    name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'

#获取case_id
def get_id():
    return global_var.Id

#获取用例名称
def get_name():
    return global_var.name

#获取url
def get_url():
    return global_var.url

#是否运行
def get_run():
    return global_var.run

def get_request_way():
    return global_var.request_way

def get_header():
    return global_var.header

def get_case_depend():
    return global_var.case_depend

def get_data_depend():
    return global_var.data_depend

def get_field_depend():
    return global_var.field_depend

def get_data():
    return global_var.data

def get_expect():
    return global_var.expect

def get_result():
    return global_var.result

def get_header_value():
    header = {
        'header':'1234',
        'cookie':'abcd'
    }
