def count_positives_sum_negatives(arr):
    if arr == []:
        new_array = []
        return new_array
    else:
        pos_sum = 0
        neg_sum = 0
        for i in arr:
            if i > 0:
                pos_sum += 1
            else:
                neg_sum += i
        new_array = [pos_sum, neg_sum]
    return new_array