# -*- coding: utf-8 -*-

# 関数：命令のまとまり
def sample(arg):
    status = arg

    if status < 10:
        return 'OK'
    else:
        return '足りません'

# リスト：配列みたいなもの
name_list = [
    'Kenji',
    'Kevin',
    'Rio',
    'Sanny'
    ]

for index in range(11):
    print(sample(index))

for item in name_list:
    print(item)

# import
# import math
# print(math.pi)

# モジュール：変数、関数、クラスなどを汎用的に使えるようにまとめたコード群
import numpy

numpy_list = [3, 1, 5, 10, 2093, 304, 123]
print(numpy.sum(numpy_list))