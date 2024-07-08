def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Zero division error"

print("Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice : ")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

if choice == '1':
    result = add(a, b)
    print("Result is :", a+b)
elif choice == '2':
    result = sub(a, b)
    print("Result is :", a-b)
elif choice == '3':
    result = mul(a, b)
    print("Result is :", a*b)
elif choice == '4':
    result = div(a, b)
    print("Result is :", a/b)
else:
    print("Invalid choice")
