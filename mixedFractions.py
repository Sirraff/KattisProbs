def main():
    arr =  []
    while (True):
        line = input()
        numerator, denominator  = [int(x) for x in line.split()]
        if(numerator == 0): 
            [print(i) for i in arr]
            return
        arr.append((f"{numerator//denominator} {numerator%denominator} / {denominator}"))
if __name__ == "__main__":
    main()
