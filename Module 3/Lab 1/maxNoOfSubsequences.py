def maximumSubsequenceCount(text, pattern):
        res = cnt1 = cnt2 = 0
        for c in text:
            if c == pattern[1]:
                res += cnt1
                cnt2 += 1
            if c == pattern[0]:
                cnt1 += 1
        return res + max(cnt1, cnt2)
        
text=input()
pattern=input()
print(maximumSubsequenceCount(text, pattern))