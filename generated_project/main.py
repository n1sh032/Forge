def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except Exception:
            # If invalid input is entered, ask again without extra messages
            continue


def main():
    a = read_int('Enter first number: ')
    b = read_int('Enter second number: ')
    print(a + b)


if __name__ == '__main__':
    main()
