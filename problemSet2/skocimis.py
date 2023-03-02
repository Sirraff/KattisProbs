def main():
    a, b, c = [int(n) for n in input().split()]
    moves = 0
    while ((c-b > 1) or (b-a > 1)): #while wither side is not touching
        # finding longest path
        if c-b > b-a:
            a, b, c = b, b+1, c
        else:
            a, b, c = a, b-1, b
        moves += 1
    print(moves)

if __name__ == "__main__":
    main()