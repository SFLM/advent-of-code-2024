def main():
    with open("example.txt") as f:
        document = f.read().splitlines()

    print(document)

if __name__ == "__main__":
    main()