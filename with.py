#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# open関数：開いたファイルに追記や解析をすることができる
# 第一引数：読み込ませたいファイルのパス、第二引数：モード(rは読みたいときに使用する)
with open('./sample.txt', 'r') as file:
    print(file)
    print(file.name)
    print(file.mode)
    # ファイルの中身を解析できる
    print(file.read())