from codrone_edu.drone import *


def quicksort(xs):
    stack = [(0, len(xs) - 1)]
    result = xs[:]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = result[start]
        left_part, right_part = partition(pivot, result[start + 1 : end + 1])

        new_section = left_part + [pivot] + right_part
        result[start : end + 1] = new_section

        pivot_index = start + len(left_part)

        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))

    return result


def partition(pivot, xs):
    left, right = [], []
    while xs != []:
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        xs = xs[1:]
    return left, right


with open("unsorted_integer.txt", "r") as file:
    lines = file.readlines()

# 문자열을 실수로 변환
numbers = [int(line.strip()) for line in lines if line.strip()]

# 퀵정렬 사용
sorted_numbers = quicksort(numbers)
with open("sorted_numbers.txt", "w") as outfile:
    for num in sorted_numbers:
        outfile.write(str(num) + "\n")

"""drone = Drone()
drone.pair()
drone.takeoff()"""
