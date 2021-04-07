def sum_of_neg_and_count_of_pos(num):
    sums = 0
    count = 0
    for i in num:
        if i < 0:
            sums += i
        else:
            count += 1
    return [count, sums]

print(sum_of_neg_and_count_of_pos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))