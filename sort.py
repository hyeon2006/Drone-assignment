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


def sorting():
    # ----------- 정렬할 파일 읽기 코드 -----------#
    with open("unsorted.txt", "r") as file:
        numbers = [int(line.strip()) for line in file if line.strip()]

    # ----------- 퀵정렬 코드 -----------#
    sorted_numbers = quicksort(numbers)
    # ----------- 파일 출력 코드 -----------#
    with open("sb-a03-c4-sorted_out.txt", "w") as outfile:
        for num in sorted_numbers:
            outfile.write(str(num) + "\n")
