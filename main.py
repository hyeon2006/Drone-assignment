from codrone_edu.drone import *


def quicksort(xs):
    if len(xs) > 1:
        pivot = xs[0]
        (left, right) = partition(pivot, xs[1:])
        return quicksort(left) + [pivot] + quicksort(right)
    else:
        return xs


def partition(pivot, xs):
    left, right = [], []
    while xs != []:
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        xs = xs[1:]
    return left, right


with open("./unsorted integer (100만개).txt", "r") as file:
    lines = file.readlines()

# 문자열을 실수로 변환
numbers = [float(line.strip()) for line in lines if line.strip()]

# 퀵정렬 사용
sorted_numbers = quicksort(numbers)
with open("sorted_numbers.txt", "w") as outfile:
    for num in sorted_numbers:
        outfile.write(str(num) + "\n")

"""drone = Drone()
drone.pair()
drone.takeoff()"""
