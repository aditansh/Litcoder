def doSomething(arr):
    max_element = 0
    chunks = 0

    for i, num in enumerate(arr):
        max_element = max(max_element, num)

        if max_element == i:
            chunks += 1

    return chunks

print(doSomething(list(map(int, input().split(" ")))))
