import sys

def longestSubstring(s):
    
    lastIdx = {}
    start = 0
    longest = 0

    for i in range(len(s)):
        if s[i] in lastIdx:
            start = max(start, lastIdx[s[i]] + 1)
        lastIdx[s[i]] = i
        longest = max(longest, i - start + 1)
    
    print(longest)



string = input()
longestSubstring(string)