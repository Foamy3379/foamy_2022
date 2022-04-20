
def count_sort(li,max_count):
    count = [0 for _ in range(max_count+1)]
    print('count',count)
    for val in li:
        count[val] += 1
    print('count',count)
    li.clear()
    for ind,val in enumerate(count):
        for i in range(val):
            li.append(ind)

import random
li = [random.randint(0,10) for _ in range(20)]
print('li',li)
count_sort(li,10)
print('li',li)

