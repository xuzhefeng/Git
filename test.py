#!/usr/local/python3/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author: edwin
# date: 2020/1/16 4:25 下午
"""

import re
# ret = re.match('a', 'abc')  # 同search,不过尽在字符串开始处进行匹配
# print(ret)

# import re
# inputStr="hello python,ni hao c,zai jian python"
# pat = re.compile("(hello python,ni hao) (\w+)(,zai jian python)")
# print(pat.findall(inputStr))
# # replaceStr=re.sub(r"(hello python,ni hao) (\w+)(,zai jian python)","\g<0>",inputStr)
# # print(replaceStr)

import os
# config_file = "conf/nginx.conf"
# config_dir, config_file = os.path.split(config_file)
# config = get_path(config_dir, cwd) + "/" + config_file
# config = 'aaaaaaaaNo such file'
# config = 'aaaaaaaaNo suc没有那个文件或目录'
config = 'aaaaaaaaNo suc'
if 'No such file' in config or '没有那个文件或目录' in config:
    print("进来了")
    # config_dir, config_file = os.path.split(config)
else:
    config_dir = ''
    config = ''
# print("config_dir:", config_dir)
print("我先修改")
