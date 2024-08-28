n = int(input("Enter any number to print the factorial: "))
def factorial(n):
    fact = 1
    if n>= 1:
        for i in range(1, n+1):
            fact = i*fact
    return fact

print(factorial(n))
