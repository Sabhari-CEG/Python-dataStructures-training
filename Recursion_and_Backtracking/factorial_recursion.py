#using the recrussive approach to find the factorial of a number.
def factorial(n):
    if n == 1:
        return 1
    f = n * factorial(n-1)
    print(f)
    return f

if __name__ == '__main__':
    print("The factorial is\t",factorial(4))