import heapq

def smallest_trimmed_numbers(nums, queries):
    ans = []
    for i in range(len(queries)):
        k, trim = queries[i]
        min_heap = []
        
        for j in range(len(nums)):
            temp = nums[j]
            res = temp[-trim:]
            heapq.heappush(min_heap, (res, j))
        
        top = None
        while min_heap and k > 0:
            res, top = heapq.heappop(min_heap)
            k -= 1
        
        ans.append(top)
        
    return ans

nums = input().split()
num_queries = int(input())

queries = []
for _ in range(num_queries):
    query = tuple(map(int, input().split()))
    queries.append(query)

output = smallest_trimmed_numbers(nums, queries)
for i in output:
    print(i, end = ' ')