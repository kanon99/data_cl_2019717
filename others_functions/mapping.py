#!/usr/bin/env pythong
# _*_ coding:utf-8 _*_
import re

#
data = [
    'tantianran phone 118',
    'tanyongxing phone 110',
    'tansufen phone 119',
    'dengwenyi phone 118',
    'dengwenqing phone 520',
    'laowang phone 110',
    'zhongjianwei 112'
]


def findes(user_input, data):
    sugge = []
    data_len = len(data)

    pat = '.*'.join(user_input)
    regex = re.compile(pat)
    for i in range(data_len):
        item = data[i]
        match = regex.search(item)
        if match:
            sugge.append(item)
            print(sugge)
            return sugge

    #print'查找结果'
    # for i in findes(strs, data):
    #     print("\033[31m %s \033[0m" % i)



if __name__ == "__main__":
    strs = input('输入查找的字符：')
    data = [
        'tantianran phone 118',
        'tanyongxing phone 110',
        'tansufen phone 119',
        'dengwenyi phone 118',
        'dengwenqing phone 520',
        'laowang phone 110',
        'zhongjianwei 112'
    ]
    findes(strs,data)
