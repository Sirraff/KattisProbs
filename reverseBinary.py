def main():
    binary = bin(int(input()))[2:]
    print(sum(2**i for i in range(len(binary)) if binary[i] == '1'))

if __name__ == "__main__":
    main()