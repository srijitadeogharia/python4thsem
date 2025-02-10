def fibonacci(n):
    fib_series=[0 , 1]
    for i in range(2 , n):
      fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

def factorial(n):
    if n == 0 or n == 1:
      return 1
    return n*factorial(n-1)

#input from user
n= int(input("Enter a number: "))

#genetating fibonacci series and factorial 
fib_num = fibonacci(n)
fact = factorial(n)

#display result
print(f"first {n} Fibonacci numbers: {fib_num}")
print(f"factorialof {n} : {fact}")