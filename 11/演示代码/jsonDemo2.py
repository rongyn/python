# 写入数据到json文件中
# 1、导包
import json
# 2、打开文件
with open(r"e:\abc.json","w",encoding="utf-8",newline="\r\n") as f:
    # 定义数据
    list1 = [
        {"name":"韩昌佩","age":28},
        {"name":"allen","age":28},
        {"name":"allen","age":28}
    ]
    # 1、使用dump函数直接将list列表写入json文件
    # json.dump(list1,f,indent=1,ensure_ascii=False)

    # 2、使用jumps转化为字符串，并通过wirte方法写入json文件
    data = json.dumps(list1,indent=1,ensure_ascii=False)
    f.write(data)
    