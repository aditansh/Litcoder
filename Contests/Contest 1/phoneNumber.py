import sys
def letter_combinations(digits):
    if not digits:
        return []

    # Define the number-to-string mapping
    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return

        current_digit = digits[index]
        if current_digit == '1':
            index += 1
            current_digit = digits[index]
        for letter in digit_map[current_digit]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations


result = letter_combinations(input())
for i in result:
    print(i, end=" ")