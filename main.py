def add(a, b):
    return a + b


def main():
    try:
        a = float(input("Vnesi prvo število (a): "))
        b = float(input("Vnesi drugo število (b): "))

        result = add(a, b)
        print(result)

    except ValueError:
        print("Napaka: vnesi števili!")


if __name__ == "__main__":
    main()