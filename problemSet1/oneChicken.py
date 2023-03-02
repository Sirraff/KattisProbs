def main():
    people, chicken = [int(x) for x in input().split()]
    if((chicken - people) > 1):
        print(f"Dr. Chaz will have {chicken - people} pieces of chicken left over!")
    elif((chicken - people) == 1):
        print(f"Dr. Chaz will have {chicken - people} piece of chicken left over!")
    elif((chicken - people) == -1):
        print(f"Dr. Chaz needs {(chicken - people)*-1} more piece of chicken!")

    elif((chicken - people) < 1):
        print(f"Dr. Chaz needs {(chicken - people)*-1} more pieces of chicken!")
if __name__ == "__main__":
    main()
