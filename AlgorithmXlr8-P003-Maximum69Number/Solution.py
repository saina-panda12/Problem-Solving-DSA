def main():
    num = input().strip()

    # Write your solution here.
    # Print the maximum number after changing at most one digit 6 to 9.
  

    num = num.replace("6", "9", 1)

    print(num)


if __name__ == "__main__":
    main()
