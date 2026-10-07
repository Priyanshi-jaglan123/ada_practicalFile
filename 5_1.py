def fractional_knapsack(weights, values, capacity):
    items = []

    # Calculate value/weight ratio
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Sort according to ratio in descending order
    items.sort(reverse=True)

    total_value = 0

    for ratio, weight, value in items:

        if capacity == 0:
            break

        if weight <= capacity:
            # Take complete item
            capacity -= weight
            total_value += value

        else:
            # Take fraction of item
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0

    return total_value


# Example
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

result = fractional_knapsack(weights, values, capacity)

print("Maximum Profit =", result)