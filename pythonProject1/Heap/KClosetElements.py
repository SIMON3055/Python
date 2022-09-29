a = [1,2,3,4,5]
k = 4
x = -1

from heapq import heapify,heappush,heappop
def findKClosestElements(a,k,x):
    res =[]
    hq = []
    print(a,k,x)

    for i in range(len(a)):
        diff = abs(x - a[i])

        if len(hq) < k:
            heappush(hq,[-1*diff,a[i]])
            # print(hq)
        else:
            element = -1 * hq[0][0]
            print(element)
            if element > diff:
                heappop(hq)
                heappush(hq, [-1 * diff, a[i]])
    # print(hq)
    for i in hq:
        res.append(i[1])
    return sorted(res)

print(findKClosestElements(a,k,x))