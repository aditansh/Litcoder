import sys
def doSomething(inval):
    map = {0:-1}
    count = 0
    maxCount = 0
    for i,j in enumerate(inval):
        if j:
            count += 1
        else:
            count -= 1
        
        if count in map:
            maxCount = max(maxCount,(i-map[count]))
        else:
            map[count] = i
    return maxCount
    
inputVal = [int(i) for i in input().split()]    
outputVal = doSomething(inputVal)
print (outputVal)