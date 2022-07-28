def fibonacci(num):
    num1 = 1
    num2 = 1

    for _ in range(num):
        print(num1, end = ' ')
        num1, num2 = num2, num1 + num2

num = int(input('Enter how many numbers needed in Fibonacci series: '))
fibonacci(num)