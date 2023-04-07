def choose_func(nums: list, func1, func2) -> list:
    negation = False
    for val in nums:
        if val <= 0:
            negation = True
    if negation:
        return remove_negatives(nums)
    else:
        return square_nums(nums)


# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums: list) -> list:
    return [num ** 2 for num in nums]


def remove_negatives(nums: list) -> list:
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25], "Wrong solution"

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5], "Wrong solution"