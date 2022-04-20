#!/usr/bin/env python
# encoding: utf-8
import time
def cal_time(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        result = end_time -start_time
        print('func time is %.9fs' % result)
        return res
    return inner


