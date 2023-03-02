# def main():
#     b_old, b_ret, b_save, a_old, a_save = [int(x) for x in input().split()]
#     total_year_b = (b_ret - b_old) * b_save
#     for i in range(1,100):
#         if (i * a_save > total_year_b):
#             print((i + a_old))
#             break
# if __name__ == "__main__":
#     main()

def main():
    b_old, b_ret, b_save, a_old, a_save = [int(x) for x in input().split()]
    total_year_b, year = (b_ret - b_old) * b_save, 1
    while (year * a_save <= total_year_b):  year += 1
    print(year + a_old)

if __name__ == "__main__":
    main()