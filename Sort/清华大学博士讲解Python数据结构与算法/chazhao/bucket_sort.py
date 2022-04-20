#!/usr/bin/env python
# encoding: utf-8
def bucket_sort(li,n=100,max_num = 10000):  # 分成100个桶 ，max_num数据的最大值
    # 不知道最大数，定义一个最大数
    bucketa = [[] for _ in range(n)] #创建桶
    for var in li:
        #决定这个数var 放到那个桶里，
        i = min(var // (max_num // n),n-1)
        #max_num// n  始终是100，var是小于100肯定在0号桶，8000肯定在80号桶，是800肯定在8号桶这个一个数据计算方法
        bucketa[i].append(var) #把var天机到桶里
        for j in range(len(bucketa[i])-1,0,-1): #这一步可以改造
            if bucketa[i][j] < bucketa[i][j-1]:
                bucketa[i][j] ,bucketa[i][j-1] = bucketa[i][j-1],bucketa[i][j]
            else:
                break
    sorted_li = []
    for buc in bucketa:
        sorted_li.extend(buc)
    return sorted_li
        # 保持桶内顺序

import random
li = [random.randint(0,10000) for i in range(100000)]
print(li)
li = bucket_sort(li)
print(li)