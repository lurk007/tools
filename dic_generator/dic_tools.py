import datetime
import hashlib
import random
import time
import os
import base64
from collections.abc import Iterable


# 编码解码


def encode_base64(s='admin', action_count=1):
    """
    base64编码
    s:字符串
    action_count:编码次数，默认一次
    :return: str
    """
    for i in range(action_count):
        s = bytes(s, 'utf-8')
        s = str(base64.b64encode(s), "utf-8")
    return s


def decode_base64(s='YWRtaW4=', action_count=1):
    """
    base64解码
    s:字符串
    action_count:编码次数
    :return: str
    """
    for i in range(action_count):
        s = bytes(s, 'utf-8')
        s = str(base64.b64decode(s), "utf-8")
    return s


def encode_md5(s='admin', action_count=1):
    """
    md5加密
    s:字符串
    action_count:加密次数
    :return: str
    """
    for i in range(action_count):
        input_name = hashlib.md5()
        input_name.update(s.encode("utf-8"))
        s = input_name.hexdigest()
    return s


def encode_buffer(s="admin", action_count=1, *funcs):
    """
    功能： 对字符串执行 任意算法 任意次数
    s: 字符串: 默认:admin
    action_count: 算法执行次数
    funcs：依次执行的算法
    return: 算法执行结果
    """
    res = s
    if len(funcs) == 0:
        funcs = [encode_md5, encode_base64]
    for i in range(action_count):
        for j in funcs:
            res = j(res)
    return res


# 生成器

def generator_date(date_start=datetime.datetime.now().strftime('%Y-%m-%d'), date_end=None, days=365, func=None,
                   action_count=1):
    """
    日期生成器
    date_start:开始日期
    days:推移天数
    func:对生成的日期执行的算法
    action_count: 算法执行次数
    """
    if func is None:
        func = str
        action_count = 0
    # 转为日期格式
    date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d')
    if date_end is not None:
        date_end = datetime.datetime.strptime(date_end, '%Y-%m-%d')
        while date_start <= date_end:
            # 日期转字符串
            s = str(date_start.strftime('%Y-%m-%d')).replace('-', '')
            for i in range(action_count):
                s = func(s)
            yield s
            days -= 1
            # 日期叠加一天
            date_start += datetime.timedelta(days=+1)
    else:
        while days > 0:
            # 日期转字符串
            s = str(date_start.strftime('%Y-%m-%d')).replace('-', '')
            for i in range(action_count):
                s = func(s)
            yield s
            days -= 1
            # 日期叠加一天
            date_start += datetime.timedelta(days=+1)


def generator_file():
    """
    创建空文件
    :return: 文件名
    """
    ran1 = int(random.random() * 1000)
    ran2 = int(random.random() * 1000)
    f_name = f"{int(round(time.time() * 1000))}r{ran1}{ran2}"
    os.system(F"type nul> {f_name}.txt")
    return f"{f_name}.txt"


def generator_id(start=0, end=1000, func=None, action_count=1):
    """
    id字符串生成器

    start: 起始id，默认0
    end:结束id，默认1000
    func:算法，默认str
    action_count:算法执行次数，默认不执行
    return: id字符串的可迭代对象
    """
    if func is None:
        func = str
        action_count = 0
    while start <= end:
        id_str = str(start)
        for i in range(action_count):
            id_str = func(id_str)
        yield id_str
        start += 1


def generator_file_buffer(func=encode_md5, action_count=1, ipt_path=None, generator=None):
    """
    功能: 对已知字典执行算法生成新的文件
    ipt_path: 已知文件相对路径
    generator:可迭代对象
    func: 对文件执行的算法，默认执行md5加密算法
    action_count:算法执行次数， 默认执行一次
    """
    opt_name = generator_file()
    while True:
        if isinstance(ipt_path, str):
            ipt = open(ipt_path)
            break
        elif isinstance(generator(), Iterable):
            ipt = generator()
            break
        else:
            return
    opt = open(opt_name, "w")
    for ipt_str in ipt:
        opt_str = ''
        for i in range(action_count):
            opt_str = func(ipt_str)
        opt.write(opt_str.replace('\n', '') + '\n')
    return opt_name


def duplicate_checking(dic1=None, dic2=None, func1=None, func2=None, action_count1=1, action_count2=1):

    if dic1 is None:
        return None
    if func1 is None:
        func1 = str
        action_count1 = 0
    if func2 is None:
        func2 = str
        action_count2 = 0
    res = dict()
    count = 0
    for i in dic1:
        s1 = i
        for a in range(action_count1):
            if func1 == str:
                break
            s1 = func1(i)
        for j in dic2:
            s2 = j
            for b in range(action_count2):
                if func2 == str:
                    break
                s2 = func2(j)
            if s1 == s2:
                print(F"对{i}执行{action_count1}次算法{func1} = 对{j}执行{action_count2}次算法{func2}")
                res.update({i: j})
                break
            count += 1
    print(F"共计校验 {count} 次，获取{len(res)}个结果")
    return res


if __name__ == '__main__':
    """test"""
    # print(encode_base64())
    # print(decode_base64())
    # print(encode_md5())
    # print(encode_buffer())
    # li = [i for i in generator_date(func=encode_md5)]
    # print([i for i in generator_id(func=encode_base64)])
    # generator_file()
    # file_name = generator_file_buffer(generator=generator_date)
    # dic = duplicate_checking(generator_date("2020-01-01", days=666), li[100:-1:21], func1=encode_md5)
