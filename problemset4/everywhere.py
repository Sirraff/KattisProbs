# Problem C
# I've Been Everywhere, Man

def count_distinct_cities():
    # Read the number of test cases
    t = int(input())

    # Iterate through each test case
    for _ in range(t):
        # Read the number of work trips
        n = int(input())

        # Create a set to store distinct cities
        cities = set()

        # Read the cities and add them to the set
        for _ in range(n):
            city = input()
            cities.add(city)

        # Print the number of distinct cities
        print(len(cities))


# Call the function to count distinct cities
count_distinct_cities()
