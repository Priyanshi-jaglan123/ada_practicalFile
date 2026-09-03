# find kth largest element

def find_kth_largest(nums, k):
    # Sort the array in descending order
    nums.sort(reverse=True)

    # k-th largest element
    return nums[k - 1]


def find_min_max(nums):
    minimum = nums[0]
    maximum = nums[0]

    for num in nums[1:]:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    return minimum, maximum


# Main program
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter the value of k: "))

# Find k-th largest
kth = find_kth_largest(nums.copy(), k)

# Find minimum and maximum
minimum, maximum = find_min_max(nums)

print("K-th largest element:", kth)
print("Minimum element:", minimum)
print("Maximum element:", maximum)
