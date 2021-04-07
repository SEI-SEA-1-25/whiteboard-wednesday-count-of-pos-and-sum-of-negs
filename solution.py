# Using a loop.
def count_positives_sum_negatives(nums):
  count = 0
  total = 0
  for num in nums:
    if num > 0:
      count += 1
    else:
      total += num

  return [count, total]

# Using list comprehensions.
def count_positives_sum_negatives(nums):
  return [len([num for num in nums if num > 0]), sum([num for num in nums if num < 0])]

# Testing it!
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
