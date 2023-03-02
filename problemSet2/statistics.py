from sys import stdin

def main():
    count, string = 1, ""
    for line in stdin:
        x = [int(n) for n in line.split()[1:]]
        string += f'Case {count}: '+ str(min(x)) + " " + str (max(x)) + " " + str(max(x)- min(x)) + "\n"
        count += 1
    print(string[:-1])
if __name__ == "__main__":
    main()