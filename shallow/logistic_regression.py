#! /user/bin/evn python
# -*- coding:utf8 -*-

"""
svm
======
A class for something.
"""

import os
import sys
import argparse
import datetime
from shallow.base_model import BaseModel
from sklearn.linear_model import LogisticRegression


# 继承shallow中的BaseModel，这样一些通用的函数就不用重复写啦。
class LR(BaseModel):
    def __init__(self, metrics_num):
        super(LR, self).__init__()
        self.model_name = 'lr'

    # 构建逻辑回归模型，直接调用sklearn提供的接口。
    def build(self):
        self.model = LogisticRegression()


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    parser = argparse.ArgumentParser(description='Process some description.')
    parser.add_argument('--phase', default='test', help='the function name.')

    args = parser.parse_args()

    if args.phase == 'test':
        print('This is a test process.')
    else:
        print("There is no {} function. Please check your command.".format(args.phase))
    end_time = datetime.datetime.now()
    print('{} takes {} seconds.'.format(args.phase, (end_time - start_time).seconds))

    print('Done svm!')
