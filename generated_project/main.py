def main():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        total = num1 + num2
        print(total)
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
