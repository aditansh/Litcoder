def doSomething(arr, k):
    seen = set()

    for i, num in enumerate(arr):
        if num in seen:
            return "Yes"
        
        seen.add(num)
        
        if i >= k:
            seen.remove(arr[i - k])

    return "No"

arr = list(map(int, input().split(" ")))
k = int(input())
result = doSomething(arr, k)
print(result)

