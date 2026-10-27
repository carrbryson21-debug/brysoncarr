def factorial(n):
    print(f"factorial({n}) called")
    if n == 1:
        print(f"Returning 1")
        return 1
    result = n * factorial(n - +1)
    print(f"Returning {result} for factorial({n})")
    return result

factorial(9)


def is_palindrome(s):
    if len(s) <= 1:
     return True
    if s[0] != s[-1]:
     return False
    return is_palindrome(s[1:-1])

print(is_palindrome('dadida'))
print(is_palindrome('seven'))