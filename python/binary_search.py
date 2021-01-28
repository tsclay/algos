from math import floor
# Assume list is sorted and only contains numbers
# Assume that target can be not found in list

# [1,3,4,5,6,8,9]


def binary_search(list, target: int):
    midpoint = 0
    left = 0
    right = len(list) - 1

    if target == list[left]:
        return left
    if target == list[right]:
        return right
    if target == list[midpoint]:
        return midpoint

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

    # if target > list[midpoint]:
    #     left = midpoint

    #     while list[left] < target:
    #         left += 1

    #     if list[left] == target:
    #         return left

    # elif target < list[midpoint]:
    #     right = midpoint

    #     while list[right] > target:
    #         right -= 1

    #     if list[right] == target:
    #         return right


sample_list = [1, 3, 4, 5, 6, 8, 9]

print(binary_search(sample_list, 6))  # 4
print(binary_search(sample_list, 3))  # 1
print(binary_search(sample_list, 5))  # 3
print(binary_search(sample_list, 9))  # 6
print(binary_search(sample_list, 10))  # -1
print(binary_search(sample_list, -1))  # -1
