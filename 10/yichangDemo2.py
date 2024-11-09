# 1、通过关键字raise手动抛出自定义
# 需求：设计方法，参数为负值，则抛出数据无效异常
# def jiaoyan(a):
#     if a<0:
#         raise Exception("不能为负数，输入异常",a)
#     else:
#         return a
# # Exception: ('不能为负数，输入异常', -2)
# print(jiaoyan(-2))


# 2、自定义异常类,继承自Exception
class myException(Exception):
    def __init__(self,code,info):
        self.code = code
        self.info = info


def jiaoyan(a):
    if a<0:
        raise myException("1001","数据无效")
    else:
        return a
# __main__.myException: ('1001', '数据无效')
print(jiaoyan(-2))