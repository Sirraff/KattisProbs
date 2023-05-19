# Read the total number of rooms & booked rooms
r, n = map(int, input().split())

# Read the booked rooms and store in a set
booked_rooms = set(int(input()) for i in range(n))

# Loop through rooms
for i in range(1, r+1):
    # if room not booked
    if i not in booked_rooms:
        print(i)
        break
else:
    print("too late")
