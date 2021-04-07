def count_positives_sum_negatives(arr):
    if arr == 0 or arr == []:
        return []
    counter = 0
    sumOfNums = 0
    for i in arr:
        if i > 0:
            counter += 1
        elif i < 0:
            sumOfNums = i + sumOfNums
    return [counter, sumOfNums]