def main():
    size, arr = int(input()), []
    
    for i in range(size):
        message, not_pow = input(), True
        length = len(message)
        power, m = 0, 0

        while(not_pow):
            if power**2 >= length:
                m, not_pow = power, False
            power += 1
        temp_arr = [[]*m]*m
        #count = 0
        message = message + '*'*((m*m) - length)
        print(message)
        # fix 2Darrays
        temp_arr[0] = 'x'
        # for i in range(m):
        #     for j in range(m):
        #         temp_arr[i][j] = message[count]
        #         count +=1
        print(temp_arr)

        print("M =", m)
                


        
if __name__ == "__main__":
    main()