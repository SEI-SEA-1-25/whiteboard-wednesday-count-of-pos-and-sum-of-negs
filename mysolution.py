# Write a function that takes in a list of numbers and gives you back a tuple or list with two items: the sum of all negative numbers in the list, and the count of all positive numbers.

# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65]. (There are 10 positive numbers, and the negative numbers add up to -65.)


# this should do it


# my solution
# Using a loop.
def pos_and_neg(nums):
  count = 0
  total = 0
  for i in nums:
    if i > 0:
      count += 1
    else:
      total += i

  return [count, total]

# Using list comprehensions.
# def count_positives_sum_negatives(nums):
  # return [len([num for num in nums if num > 0]), sum([num for num in nums if num < 0])]

# Testing it!
print(pos_and_neg([1, 5,-2, -4, 7, 8,1, 3]))