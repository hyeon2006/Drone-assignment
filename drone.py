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
st = timeC.timestart()
drone.pair()
drone.speed_change(1)
drone.drone_LED_off()

format()
buzz()
drone.takeoff()
up(50, 1)
# 첫 허들 시작
forward(50, 3.25)
down(70, 3.9)
forward(50, 2.4)
# 첫번째 허들 완, 두번째 허들 시작
up(46, 3.1)
forward(50, 2.6)
# 두번째 허들 완, 세번째 허들 시작
down(70, 3.0)
forward(50, 1.9)
# 세번째 허들 완
up(80, 1.5)
spinL(100, 1.35)
drone.hover(1)
buzz()
forward(50, 2.3)
left(50, 1)
backward(50, 1)
right(50, 1)
drone.hover(1)
forward(51, 3)
spinL(100, 1.35)
drone.hover(1)
buzz()

drone.hover(5)
sort.sorting()

forward(50, 5)


drone.land()
buzz()
drone.close()
timeC.timeend(st)
