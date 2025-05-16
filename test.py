from codrone_edu.drone import *
import sort


def format():
    drone.set_throttle(0)
    drone.set_pitch(0)
    drone.set_roll(0)
    drone.set_yaw(0)


def forward(power, duration):
    """
    전방으로 비행

    :param power: 비행속도
    :param duration: 비행시간
    """
    drone.set_pitch(power)
    drone.move(duration)
    drone.set_pitch(0)


def backward(power, duration):
    """
    후방방으로 비행

    :param power: 비행속도
    :param duration: 비행시간
    """
    drone.set_pitch(-power)
    drone.move(duration)
    drone.set_pitch(0)


def up(power, duration):
    """
    위로 비행

    :param power: 비행속도
    :param duration: 비행시간
    """
    drone.set_throttle(power)
    drone.move(duration)
    drone.set_throttle(0)


def down(power, duration):
    """
    아래로 비행

    :param power: 비행속도
    :param duration: 비행시간
    """
    drone.set_throttle(-power)
    drone.move(duration)
    drone.set_throttle(0)


def spinL(power, duration):
    """
    왼쪽방향으로 회전

    :param power: 비행속도
    :param duration: 비행시간
    """
    drone.set_yaw(power)
    drone.move(duration)
    drone.set_yaw(0)


def spinR(power, duration):
    """
    오른쪽방향으로 회전

    :param power: 비행속도
    :param duration: 비행시간
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

up(40, 1)
forward(28, 4.5)
down(30, 3.75)
forward(35, 2)
up(40, 5)
forward(30, 3.5)
down(30, 6)
forward(30, 2.5)
up(30, 4)
spinL(25, 3)
# buzz()
forward(30, 2)
spinL(25, 4)
forward(30, 4)
spinL(30, 10)
# buzz()
drone.hover(5)
# sort.sorting()


drone.land()

drone.close()
