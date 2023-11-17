def sliding_subarray_beauty(arr, k, n):
    result = []

    def nth_smallest_in_subarray(subarray, n):
        sorted_subarray = sorted(subarray)
        return sorted_subarray[n - 1]

    current_subarray = arr[:k]

    result.append(nth_smallest_in_subarray(current_subarray, n))

    for i in range(k, len(arr)):
        current_subarray.pop(0)
        current_subarray.append(arr[i])
        result.append(nth_smallest_in_subarray(current_subarray, n))

    return result

arr = list(map(int, input().split()))
k = int(input())
n = int(input())
result = sliding_subarray_beauty(arr, k, n)
for i in result:
    print(i, end=" ")
