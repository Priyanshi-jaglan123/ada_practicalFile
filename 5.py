# Program 5: Fractional Knapsack and Job Scheduling

# ---------- Fractional Knapsack ----------
def fractional_knapsack(weights, values, capacity):

    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Sort by value/weight ratio
    items.sort(reverse=True)

    total_profit = 0

    for ratio, weight, value in items:

        if capacity == 0:
            break

        if weight <= capacity:
            capacity -= weight
            total_profit += value
        else:
            fraction = capacity / weight
            total_profit += value * fraction
            capacity = 0

    return total_profit


# ---------- Job Scheduling ----------
def job_scheduling(jobs):

    # Sort jobs according to profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [None] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in jobs:

        for i in range(min(deadline, max_deadline) - 1, -1, -1):

            if slots[i] is None:
                slots[i] = job_id
                total_profit += profit
                break

    return slots, total_profit


# ---------- Main Program ----------

print("Fractional Knapsack and Job Scheduling")

# Fractional Knapsack
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

profit = fractional_knapsack(weights, values, capacity)

print("\nFractional Knapsack")
print("Maximum Profit =", profit)


# Job Scheduling
jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]

schedule, job_profit = job_scheduling(jobs)

print("\nJob Scheduling")
print("Job Sequence =", schedule)
print("Maximum Profit =", job_profit)