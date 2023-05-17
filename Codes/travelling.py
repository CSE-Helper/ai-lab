import sys


def tsp_dp(cities, start_city):
    n = len(cities)
    # Initialize memoization table
    memo = [[-1] * (1 << n) for _ in range(n)]

    # Helper function to calculate the minimum cost
    def dp(current, visited):
        if visited == (1 << n) - 1:
            return cities[current][start_city]
        if memo[current][visited] != -1:
            return memo[current][visited]

        min_cost = sys.maxsize
        for next_city in range(n):
            if visited & (1 << next_city) == 0:
                cost = cities[current][next_city] + \
                    dp(next_city, visited | (1 << next_city))
                min_cost = min(min_cost, cost)

        memo[current][visited] = min_cost
        return min_cost

    return dp(start_city, 1 << start_city)


def main():
    n = int(input("Enter the number of cities: "))

    # Create a matrix to store city distances
    cities = [[float('inf')] * n for _ in range(n)]

    # Input the distances between cities
    for i in range(n):
        for j in range(n):
            if i == j:
                cities[i][j] = 0
            else:
                distance = input(
                    f"Enter the distance between city {i+1} and city {j+1} (or $ for infinity): ")
                if distance != "$":
                    cities[i][j] = int(distance)

    start_city = int(input("Enter the starting city (1 to N): ")) - 1

    # Solve the TSP problem
    min_cost = tsp_dp(cities, start_city)

    print(
        f"The minimum cost of the TSP tour starting from city {start_city+1} is: {min_cost}")


if __name__ == "__main__":
    main()
