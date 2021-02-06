#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# クラス
class Card:
    # __init__：コンストラクタ（インスタンスの生成時のみ呼ばれる特殊な関数）
    # self：thisみたいなもの（インスタンスを呼び出したとき、それ自身がselfに入る）

    # メソッド：クラスの中で定義されている関数
    def __init__(self, date, user_name):
        # プロパティ：クラスの中で定義されている変数
        self.date = date
        self.user_name = user_name

    def message(self):
        print('この投稿は' + self.user_name + 'さんによって' + self.date + 'に投稿されました')

date_a = '2020-02-01'
user_name_a = 'Taro'
card_a = Card(date_a, user_name_a)

date_b = '2020-02-21'
user_name_b = 'Kanako'
card_b = Card(date_b, user_name_b)

card_a.message()
card_b.message()