from codrone_edu.drone import *
import main


def forward(times):
    """
    전방으로 1초간 비행

    :param times: 비행횟수, 높은 고도에서 3회 비행시 약 1m 비행
    """
    for i in range(times):
        drone.set_pitch(30)
        drone.move(1)
        drone.set_pitch(0)


def backward(times):
    """
    후방으로 1초간 비행

    :param times: 비행횟수, 높은 고도에서 3회 비행시 약 1m 비행
    """
    for i in range(times):
        drone.set_pitch(-30)
        drone.move(1)
        drone.set_pitch(0)


def up(times):
    """
    위로 1초간 비행

    :param times: 비행횟수,
    """
    for i in range(times):
        drone.set_throttle(30)
        drone.move(1)
        drone.set_throttle(0)


def down(times):
    """
    아래로 1초간 비행

    :param times: 비행횟수,
    """
    for i in range(times):
        drone.set_throttle(-30)
        drone.move(1)
        drone.set_throttle(0)


def spinL(times):
    """
    왼쪽으로 1초간 회전

    :param times: 회전횟수
    """
    for i in range(times):
        drone.set_yaw(25)
        drone.move(1)
        drone.set_yaw(0)


def spinR(times):
    """
    오른쪽으로 1초간 회전

    :param times: 회전횟수
    """
    for i in range(times):
        drone.set_yaw(-25)
        drone.move(1)
        drone.set_yaw(0)


def buzz():
    drone.drone_buzzer(Note.C4, 500)
    drone.drone_buzzer(Note.D4, 500)
    drone.drone_buzzer(Note.E4, 500)
    drone.drone_buzzer(Note.F4, 500)
    drone.drone_buzzer(Note.G4, 500)


drone = Drone()

# 드론 페어링
drone.pair()
# buzz()
drone.takeoff()

up(1)
forward(4)
down(3)
forward(2)
up(8)
forward(3)
down(6)
forward(2)
up(6)
spinL(2)
# buzz()
forward(12)
spinL(6)
forward(3)
spinL(1)
# buzz()
drone.hover(5)
# main.sorting()


drone.land()

drone.close()
