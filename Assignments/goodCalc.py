#add a+b
def add(a, b):
    return a + b
#subtract a and b
def subtract(a, b):
    return a - b
#multiply a and b
def multiply(a, b):
    return a * b
#get input
def get_input():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def main():
    a, b = get_input()
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")

if __name__ == "__main__":
    main()
