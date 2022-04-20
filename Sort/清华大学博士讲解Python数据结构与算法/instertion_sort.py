
def instertion_stor(li):
    lit=[]
    for i in range(0,len(li)):
        lit.append(li[i])
        j = len(lit)-1
        while lit[j] < lit[j-1] and j >= 1:
            lit[j],lit[j-1] = lit[j-1],lit[j]
            j -= 1
        print(lit)
import random
li = list(range(18))
random.shuffle(li)
# print(li)
# instertion_stor(li)
# print(li)

def instertion_stor_y(li):
    for i in range(0,len(li)):
        tot = i
        while li[tot] > li[tot-1] and tot >=1 :
            li[tot],li[tot-1] = li[tot-1],li[tot]
            tot -= 1
print(li)
instertion_stor_y(li)
print(li)

print((4+8)/2)