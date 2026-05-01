def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Deljenje z 0 ni dovoljeno")
    return a / b


def main():

    while True:
        print("1. +")
        print("2. - ")
        print("3. *")
        print("4. /")
        print("5. ")

        choice = input("\nVnesi izbiro (1-5): ").strip()

        if choice == '5':
            break

        try:
            a = float(input("Vnesi prvo število (a): "))
            b = float(input("Vnesi drugo število (b): "))
        except ValueError:
            continue

        try:
            if choice == '1':
                result = add(a, b)
                print(f"\n{a} + {b} = {result}")
            elif choice == '2':
                result = subtract(a, b)
                print(f"\n{a} - {b} = {result}")
            elif choice == '3':
                result = multiply(a, b)
                print(f"\n{a} * {b} = {result}")
            elif choice == '4':
                result = divide(a, b)
                print(f"\n{a} / {b} = {result}")
        except ValueError as e:
            print(f"\nNapaka: {e}")


if __name__ == "__main__":
    main()
