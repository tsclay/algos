# Assume list is sorted and only contains numbers
# Assume that target can be not found in list

# [1,3,4,5,6,8,9]


def binary_search(list, target: int):
    midpoint = 0
    left = 0
    right = len(list) - 1

    # Check if target happens to be max, min, or mid value already
    if target == list[left]:
        return left
    if target == list[right]:
        return right
    if target == list[midpoint]:
        return midpoint

    # Check if target is larger than the max or smaller than the min
    if target > list[right] or target < list[left]:
        return -1

    while left <= right:
        midpoint = (left + right) // 2

        if list[midpoint] < target:
            left = midpoint + 1

        elif list[midpoint] > target:
            right = midpoint - 1

        else:
            return midpoint

    # Target falls within min-max, but is not found
    return -1


sample_list = [1, 3, 4, 5, 6, 8, 9]

print(binary_search(sample_list, 6))  # 4
print(binary_search(sample_list, 3))  # 1
print(binary_search(sample_list, 5))  # 3
print(binary_search(sample_list, 9))  # 6
print(binary_search(sample_list, 10))  # -1
print(binary_search(sample_list, -1))  # -1
