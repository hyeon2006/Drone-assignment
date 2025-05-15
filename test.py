from codrone_edu.drone import *
import main


def format():
    drone.set_throttle(0)
    drone.set_pitch(0)
    drone.set_roll(0)
    drone.set_yaw(0)


def forward(power, duration):
    """
    전방으로 1초간 비행

    :param times: 비행횟수, 높은 고도에서 3회 비행시 약 1m 비행
    """
    drone.set_pitch(power)
    drone.move(duration)
    drone.set_pitch(0)


def backward(power, duration):
    """
    후방으로 1초간 비행

    :param times: 비행횟수, 높은 고도에서 3회 비행시 약 1m 비행
    """
    drone.set_pitch(-power)
    drone.move(duration)
    drone.set_pitch(0)


def up(power, duration):
    """
    위로 1초간 비행

    :param times: 비행횟수,
    """
    drone.set_throttle(power)
    drone.move(duration)
    drone.set_throttle(0)


def down(power, duration):
    """
    아래로 1초간 비행

    :param times: 비행횟수,
    """
    drone.set_throttle(-power)
    drone.move(duration)
    drone.set_throttle(0)


def spinL(power, duration):
    """
    왼쪽으로 1초간 회전

    :param times: 회전횟수
    """
    drone.set_yaw(power)
    drone.move(duration)
    drone.set_yaw(0)


def spinR(power, duration):
    """
    오른쪽으로 1초간 회전

    :param times: 회전횟수
    """
    drone.set_yaw(-power)
    drone.move(duration)
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
format()
# buzz()
drone.takeoff()

forward(28, 5)
down(30, 1)
forward(35, 2)
up(40, 5)
forward(30, 4)
down(30, 4)
forward(30, 3)
up(30, 4)
spinL(25, 3)
# buzz()
forward(30, 4)
spinL(25, 6)
forward(30, 4)
spinL(25, 8)
# buzz()
drone.hover(5)
# main.sorting()


drone.land()

drone.close()
