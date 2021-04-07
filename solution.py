def count_positive_sum_neg(arr):
    if not arr:
        return []

    pos = 0
    neg = 0

    for x in arr:
        if x > 0:
            pos += 1
        if x < 0:
            neg += 1
    return [pos, neg]
