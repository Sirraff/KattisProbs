def main():
    word, dict = input(), {}
    for item in ''.join(set(word)):
        dict[item] = word.count(item)
        for key in dict:
            dict[key] = 1 if (dict[key]%2 != 0) else 0
    print (sum(x for x in dict.values()) - 1) if sum(x == 1 for x in dict.values())-1 > 1 else print(0)
if __name__ == "__main__":
    main()