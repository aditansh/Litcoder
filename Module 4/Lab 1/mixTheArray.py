def mix_the_array(initial_size, query_count, queries):
    array = [0] * initial_size

    for query in queries:
        start_idx, end_idx, value = query
        array[start_idx - 1:end_idx] = [x + value for x in array[start_idx - 1:end_idx]]

    return max(array)

initial_size = int(input().strip())
query_count = int(input().strip())

queries = []
for _ in range(query_count):
    query = list(map(int, input().strip().split()))
    queries.append(query)

result = mix_the_array(initial_size, query_count, queries)
print(result)