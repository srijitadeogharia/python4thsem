def is_palindorm(s):
    return s==s[::-1]

N=input("Enter a string")

if is_palindorm(N):
    print("true")
else:
    print("false")

