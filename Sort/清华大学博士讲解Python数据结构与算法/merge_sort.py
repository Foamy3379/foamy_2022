#!/usr/bin/env python
# encoding: utf-8

def merge(li,low,mid,high):
    i = low
    j = mid+1
    ltmp = []
    while i <= mid and j <=high:#只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while 执行安成，肯定有一部分没有完成
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j +=1 
    li[low:high+1] = ltmp

# li = [2,4,5,7,1,3,6,8]
# merge(li,0,3,7)

# print(li)


def merge_sort(li,low,high):
    if low < high: #至少有两个元素，递归
        mid = (low + high) //2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        print(li[low:high+1])
        merge(li,low,mid,high)

# def merge_sort_test(li,low,high):
#     if low < high:#至少有两个元素
#         mid = (low+high)//2
#         merge_sort_test(li,low,mid)
#         merge_sort_test(li,mid+1,high)
#         print(li[low:high+1])
li = list(range(16))
import random
random.shuffle(li)
print(li)
merge_sort(li,0,len(li)-1)
print(li)


# 时间复杂度
# 空间复杂度