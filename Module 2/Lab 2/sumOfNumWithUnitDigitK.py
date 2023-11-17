def minSetSize(k,sum):
    if sum == 0:
        return 0
    for i in range(1,10):
        if (i*k)<=sum and (k*i)%10 == sum%10:
            return i
    return -1

k = int(input())
sum = int(input())

print(minSetSize(k, sum))