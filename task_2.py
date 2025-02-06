def binary_search_recursive(arr, target, left, right, iterations=0, upper_bound=None):
    if left > right:
        return f'iterations: {iterations}\nupper_bound: {upper_bound}\ntarget: Not Found'

    iterations += 1
    mid = (left + right) // 2

    if arr[mid] == target:
        return f'iterations: {iterations}\nupper_bound: {upper_bound}\ntarget: {arr[mid]}'

    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, iterations, upper_bound)
    else:
        upper_bound = arr[mid]
        return binary_search_recursive(arr, target, left, mid - 1, iterations, upper_bound)

arr = [1, 2, 3, 4, 5, 6]

result = binary_search_recursive(arr, 5, 0, len(arr) - 1)
result2 = binary_search_recursive(arr, 7, 0, len(arr) - 1)

print(result)  # (3, 5)
print("----------------------")
print(result2)  # (3, None)
