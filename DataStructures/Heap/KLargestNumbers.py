print("helloworld")

a = [1,76,89,65,4,3,6,8,9]
k =3
from heapq import heapify,heappop, heappush,heappushpop
def maxKNumber(a,k):
    n = len(a)
    hq = []
    res = []
    for i in a:
        heappush(hq,-1 * i)
    
    count = 1
    while count < k:
        res.append(-1 * heappop(hq))
        count+=1
        
    return res
print(maxKNumber(a,k))