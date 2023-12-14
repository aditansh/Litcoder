def is_balanced(s):
    stack = []
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_mapping.values():
            stack.append(char)
        elif char in bracket_mapping.keys():
            if not stack or stack.pop() != bracket_mapping[char]:
                return "NO"
        else:
            pass
           
    return "YES" if not stack else "NO"

input_strings = input().split(',')
for s in input_strings:
    print(is_balanced(s))