nums = [2,2,2,3]

from collections import defaultdict,Counter
class Array:
    def singleNumber(a):
        n = len(a)
        list_dict = defaultdict(int)
        for i in range(n):
            list_dict[a[i]]+=1

        for k,v in list_dict.items():
            if v==1:
                return k

    def singleNumber2(a):
        n = len(a)

        hashmap = Counter(a)
        print(hashmap)
        for k,v in hashmap.items():
            if v==1:
                return k

print(Array.singleNumber((nums)))
print(Array.singleNumber2((nums)))
