# Program 2: Merge Sort and Quick Sort

class Sort:

    def merge_sort(self, arr):
        """Sort the array using Merge Sort."""

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        """Merge two sorted arrays."""

        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def quick_sort(self, arr):
        """Sort the array using Quick Sort."""

        if len(arr) <= 1:
            return arr

        pivot = arr[-1]

        left = []
        middle = []
        right = []

        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

        return (
            self.quick_sort(left)
            + middle
            + self.quick_sort(right)
        )


# Main program
arr = list(map(int, input("Enter array elements: ").split()))

print("Array:", arr)

obj = Sort()

print("\nOriginal array:", arr)

merge_result = obj.merge_sort(arr)
print("After Merge Sort:", merge_result)

quick_result = obj.quick_sort(arr)
print("After Quick Sort:", quick_result)