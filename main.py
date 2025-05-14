from codrone_edu.drone import *
import time


def quicksort(xs):
    if len(xs) > 1:
        pivot = xs[0]
        (left, right) = partition(pivot, xs[1:])
        return quicksort(left) + [pivot] + quicksort(right)
    else:
        return xs


def partition(pivot, xs):
    left, right = [], []
    for x in xs:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left, right


# ----------- 타이머 코드 -----------#
start_time = time.time()
# ----------- 정렬할 파일 읽기 코드 -----------#
with open("unsorted integer (100만개 샘플).txt", "r") as file:
    numbers = [int(line.strip()) for line in file if line.strip()]

# ----------- 퀵정렬 코드 -----------#
sorted_numbers = quicksort(numbers)
# ----------- 파일 출력 코드 -----------#
with open("sorted_numbers.txt", "w") as outfile:
    for num in sorted_numbers:
        outfile.write(str(num) + "\n")

# ----------- 시간 코드 -----------#
end_time = time.time()

elapsed_time = round(end_time - start_time)

print(f"정렬에 걸린 시간: {elapsed_time}초")
