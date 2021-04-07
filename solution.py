# Using a loop 

def count_positives_sum_negatives(nums):
    count = 0
    total = 0
    for num in nums:
        if num > 0:
            count += 1
        else: 
            total += num
    return [count, total]
ﬁ
# Using list comprehensions.

def count_positives_sum_negatives(nums):
    return [len([num for num in nums if num > 0]), sum([num for num in nums if num < 0])]

# Testing it!

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -15, -15]))


def unique_in_order(iterable):
    result = []
    prev = None
    for element in iterable:
        if element != prev:
            result.append(element)
            prev = element 
    return result 

def unique_in_order(iterable):
    result = []
    for element in iterable:
        if len(result) == 0 or element != result[-1]:
            result.append(element)
    return result 


