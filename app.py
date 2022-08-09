def main():
    filename = input("Enter filename: ")

    with open(filename, "r") as file:
        data = file.read()

    print(f"Data: {data}")

if __name__ == "__main__":
    main()
