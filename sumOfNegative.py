numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

def sum_and_count(arr):
    positive = 0
    negative = 0
    for i in arr:
        if i >= 0:
            positive = positive + 1
        elif i < 0:
            negative = negative + i
            
    return [positive, negative]

print(sum_and_count(numbers))

