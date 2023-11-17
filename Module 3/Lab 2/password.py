def check_passwords(passwords):
    passwords.sort()  # Sort the passwords to make it easier to check prefixes

    for i in range(len(passwords) - 1):
        if passwords[i + 1].startswith(passwords[i]):
            return "BAD PASSWORD"
    return "GOOD PASSWORD"

passwords = input().split()
print(check_passwords(passwords))
