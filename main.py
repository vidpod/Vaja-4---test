def add(a, b):
    return a + b


def main():

        a = float(input("Vnesi prvo število (a): "))
        b = float(input("Vnesi drugo število (b): "))

        result = add(a, b)
        print(result)


if __name__ == "__main__":
    main()
