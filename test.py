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
    후방으로 비행

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


def right(power, duration):
    """
    오른쪽방향으로 이동

    :param power: 비행속도
    :param duration: 비행시간
    """
    drone.set_roll(power)
    drone.move(duration)
    drone.set_roll(0)


def left(power, duration):
    """
    왼쪽방향으로 이동

    :param power: 비행속도
    :param duration: 비행시간
    """
    drone.set_roll(-power)
    drone.move(duration)
    drone.set_roll(0)


def buzz():
    drone.drone_buzzer(Note.C4, 300)
    drone.drone_buzzer(Note.D4, 300)
    drone.drone_buzzer(Note.E4, 300)
    drone.drone_buzzer(Note.F4, 300)
    drone.drone_buzzer(Note.G4, 300)


drone = Drone()

# 드론 페어링
drone.pair()
drone.drone_LED_off()
format()
buzz()
drone.takeoff()

up(40, 2)
forward(28, 4.75)
down(30, 2.4)
forward(35, 2.25)
up(40, 4)
forward(30, 3.25)
down(30, 3.25)
forward(30, 3)
up(30, 4)
spinL(20, 1.5)
buzz()
forward(30, 4)
left(30, 2)
backward(30, 2)
right(30, 2)
forward(30, 4)
spinL(25, 1.5)
buzz()

drone.hover(5)
sort.sorting()

forward(30, 6.5)


drone.land()
buzz()
drone.close()
