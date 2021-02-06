# -*- coding: utf-8 -*-
class Sample:
    # コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 成人かチェックする関数
    def judge(self):
        if self.age >= 20:
            print(self.name + 'さんは' + '成人です')
        else:
            print(self.name + 'さんは' + '成人ではありません')


# リストを定義
name = ['Sato', 'Takahashi', 'Yamada', 'Inoue', 'Goto']
age = [23, 19, 30, 17, 27]

# インスタンス化
sample_a = Sample(name[4], age[1])
# 関数の呼び出し
sample_a.judge()

# インスタンス化
sample_b = Sample(name[1], age[0])
# 関数の呼び出し
sample_b.judge()