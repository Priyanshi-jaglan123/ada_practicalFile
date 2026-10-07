def job_scheduling(jobs):
    # Sort jobs according to profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    slots = [None] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in jobs:

        # Find an empty slot before deadline
        for i in range(min(deadline, max_deadline) - 1, -1, -1):

            if slots[i] is None:
                slots[i] = job_id
                total_profit += profit
                break

    return slots, total_profit


# Example
jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]

schedule, profit = job_scheduling(jobs)

print("Job Sequence:", schedule)
print("Maximum Profit:", profit)