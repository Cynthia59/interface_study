class CommonUtil:
    def is_contain(self, kid_str, str):
        '''
        判断一个字符串是否在另一个字符串中
        :return:
        '''
        flag = None
        # if isinstance(kid_str, unicode):

        if kid_str in str:
            flag = True
        else:
            flag = False
        return flag