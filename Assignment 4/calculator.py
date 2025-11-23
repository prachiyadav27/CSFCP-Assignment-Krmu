# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")
    
    while True:
        choice = input("\nEnter operation (+ - * /) or 'q' to quit: ").strip()
        
        if choice == 'q':
            print("Thank you for using the calculator!")
            break
            
        if choice not in ['+', '-', '*', '/']:
            print("Invalid operation!")
            continue
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        
        if choice == '+':
            print(f"Result: {add(num1, num2)}")
        elif choice == '-':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '*':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '/':
            print(f"Result: {divide(num1, num2)}")

if __name__ == "__main__":
    main()