

import heapq  #q ->queue δΌειε
from operator import le
import random
li = list(range(100))
random.shuffle(li)
print(li)
heapq.heapify(li)
n = len(li)
for i in range(n):
    print(heapq.heappop(li),end=',')