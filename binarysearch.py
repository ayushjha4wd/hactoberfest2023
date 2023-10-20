def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        mid_element = arr[mid]  # Get the middle element

        # Check if the middle element is the target
        if mid_element == target:
            return mid  # Target found, return the index

        # If the target is smaller, ignore the right half
        elif mid_element > target:
            right = mid - 1

        # If the target is larger, ignore the left half
        else:
            left = mid + 1

    return -1  # Target not found in the list

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
