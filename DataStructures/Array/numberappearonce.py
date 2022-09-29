a = [1,2,3,4,3,2,1,]

def appearonce(a):
    res = 0
    for i in a:
        res = res ^ i

    return res
print(appearonce(a))