def earliest_party(n, trees):
    # Sort array descendingly
    trees.sort(reverse=True)
    max_days = 0
    for i in range(n):
        # current tree time to grow
        total_days = trees[i] + i + 1
        # Update the max
        max_days = max(max_days, total_days)
    # maximum number of days +1 for the party day
    return max_days + 1

n = int(input().strip())
trees = list(map(int, input().strip().split()))
print(earliest_party(n, trees))
