def minSteps(candies, target):
    steps = 0
    candies.sort()

    while candies[0] < target:
        new_sweetness = candies[0] + 2 * candies[1]
        candies = [new_sweetness] + candies[2:]
        candies.sort()
        steps += 1

    return steps

target = int(input())
candies = list(map(int, input().split()))
print(minSteps(candies, target))