def f(n):
    if n <= 1:
        return n

    return f(n - 1) + f(n - 2)


def main():
    n = int(input())
    result = f(n)
    print(result)


if __name__ == "__main__":
    main()