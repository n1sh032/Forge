def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        total = num1 + num2
        # If the numbers are whole, display as int for cleaner output matching test expectations
        if total.is_integer():
            print(int(total))
        else:
            print(total)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
