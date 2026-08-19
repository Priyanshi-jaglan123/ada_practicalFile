# Program 1: Search and Power Functions

def search(nums, target):
    """
    Search for target in a sorted array using Binary Search.
    Returns the index if found, otherwise -1.
    """
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def myPow(x, n):
    """
    Calculate x raised to the power n using Divide and Conquer.
    """
    if n == 0:
        return 1

    if n < 0:
        return 1 / myPow(x, -n)

    half = myPow(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


# Main program
nums = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target element: "))

result = search(nums, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")


x = float(input("Enter the base: "))
n = int(input("Enter the exponent: "))

print("Power =", myPow(x, n))