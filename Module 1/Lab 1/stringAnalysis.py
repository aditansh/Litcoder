import sys
def doSomething(inval):
    freq = {
        "upper":0,
        "lower":0,
        "digits":0,
        "others":0
    }
    
    length = len(inval)
    
    for i in inval:
        if i.isalpha():
            if i.isupper():
                freq['upper'] += 1
            else:
                freq["lower"] += 1
        elif i.isdigit():
            freq["digits"] += 1
        else:
            freq["others"] += 1
    
    for i in freq:
        freq[i] /= length
        freq[i] *= 100
        
    print("%.3f%%\n%.3f%%\n%.3f%%\n%.3f%%" %(freq["upper"],freq["lower"],freq["digits"],freq["others"]))
        
inputVal = input()
doSomething(inputVal)