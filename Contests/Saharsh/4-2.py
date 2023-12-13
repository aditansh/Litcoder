def doSomething(n, jobs, deadlines, profits):
    job_order = sorted(range(n), key=lambda k: profits[k], reverse=True)

    result = [None] * n
    slot = [False] * n

    for i in range(n):
        for j in range(min(deadlines[job_order[i]] - 1, n-1), -1, -1):
            if not slot[j]:
                result[j] = jobs[job_order[i]]
                slot[j] = True
                break

    return " ".join([job for job in result if job is not None])

n = int(input())
jobs = input().split(" ")
deadlines = list(map(int, input().split()))
profits = list(map(int, input().split()))
outputVal = doSomething(n, jobs, deadlines, profits)
print (outputVal)

