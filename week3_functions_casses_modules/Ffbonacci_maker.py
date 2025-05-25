def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input('Which Fibonacci number would you like? '))

print(f'It is {fibonacci(number-1)}.')