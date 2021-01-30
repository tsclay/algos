# Reverse a string

# Using special Python slicing syntax, includes all characters
def ez_reverse(string: str) -> str:
    return string[::-1]

# Longer solution using pointers


def reverse(string: str) -> str:
    left = 0
    right = len(string) - 1
    str_list = list(string)

    while left < right:
        old_right = str_list[right]
        old_left = str_list[left]
        str_list[left] = old_right
        str_list[right] = old_left
        left += 1
        right -= 1

    output = ''.join(str_list)

    return output


print(reverse('01234'))  # 43210
print(reverse('I have a dog.'))  # .god a evah I
print(ez_reverse('Hello'))
