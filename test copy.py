from codrone_edu.drone import *
import sort
import timeC


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
st = timeC.timestart()
up(40, 1.1)
forward(28, 4)
down(50, 4)
forward(35, 1.75)
# 첫번째 허들 완
up(40, 2.5)
forward(30, 2.75)
# 두번째 허들 완
down(50, 3)
forward(30, 2.1)
up(50, 2)
spinL(25, 2.65)
drone.hover(1)
buzz()
forward(30, 4)
left(40, 1)
backward(40, 1)
right(40, 1)
forward(30, 3.25)
spinL(25, 2.8)
drone.hover(1)
buzz()

drone.hover(5)
sort.sorting()

forward(30, 6.5)


drone.land()
buzz()
drone.close()
timeC.timeend(st)
