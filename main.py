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


with open("numbers.txt", "r") as file:
    lines = file.readlines()

drone = Drone()
drone.pair()
drone.takeoff()
