#!/usr/bin/env python
# encoding: utf-8

def sift(li,low,high):
    """
    li:列表
    low: 堆的根节点位置
    high: 堆的最后一个元素的位置
    """
    i = low #最开始的位置
    j = 2*i + 1 #j开始时左孩子
    tmp = li[low] #把对顶存起来
    while j <= high: #只要j位置有数
        if j + 1 <= high and li[j+1] < li[j]: #如果右孩子存在并且比左孩子大
            j = j+1 #j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j    #往下看一层
            j = 2*i +1
        else:  #tmp更大 把tmp放到i的位置上
            li[i] = tmp  #把tmp放到某一级领导位置
            break
    else:
        li[i] = tmp # 把tmp放到叶子节点上
def topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap,i,k-1)
    #1 建堆
    for i in range(k,len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap,0,k-1)
    # 2 遍历
    for i in range(k-1,-1,-1):
        #i指向当前堆的最后一个元素
        heap[0],heap[i] = heap[i],heap[0]
        sift(heap,0,i-1) #i-1是洗呢high
    # 3 出数
    return heap


import random
li = list(range(1000))
# print(li)
random.shuffle(li)
# print(li)
print(topk(li,10))