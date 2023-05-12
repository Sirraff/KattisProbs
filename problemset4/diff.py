# Problem B
# Detailed Differences

def identify_differences():
    n = int(input())

    for _ in range(n):
        # Read the two input strings
        str1 = input()
        str2 = input()

        # Compare the chars in the two strings
        result = ['.' if c1 == c2 else '*' for c1, c2 in zip(str1, str2)]

        # Convert the result list back to a string
        result = ''.join(result)

        print(str1)
        print(str2)
        print(result)
        print()

identify_differences()
