from codrone_edu.drone import *
from time import sleep

drone = Drone()

# 드론 페어림
drone.pair()

# 시작 시간 측정

# #버저 5회 작동
# drone.drone_buzzer(Note.C4, 500)
# drone.drone_buzzer(Note.D4, 500)
# drone.drone_buzzer(Note.E4, 500)
# drone.drone_buzzer(Note.F4, 500)
# drone.drone_buzzer(Note.G4, 500)

# 드론 이륙
drone.takeoff()

# 상승
drone.set_throttle(30)
drone.move(1)
drone.set_throttle(0)
# 전진
drone.set_pitch(30)
drone.move(2.5)
drone.set_pitch(0)

# 하강
drone.set_throttle(-70)
drone.move(2)
drone.set_throttle(0)
# ---#
# 전진
drone.set_pitch(30)
drone.move(2)
drone.set_pitch(0)
drone.hover(1)

# 상승
drone.set_throttle(70)
drone.move(2.5)
drone.set_throttle(0)
# 전진
drone.set_pitch(25)
drone.move(2.25)
drone.set_pitch(0)
drone.hover(0.5)
# 하강
drone.set_throttle(-70)
drone.move(2.5)
drone.set_throttle(0)
"""
# 하강
drone.set_throttle(-20)
drone.move(2.5)
drone.set_throttle(0)

# 드론 호버링
drone.hover(3)

# 전진
drone.set_pitch(20)
drone.move(3)
drone.set_pitch(0)

# 드론 호버링
drone.hover(2)

# 상승
drone.set_throttle(25)
drone.move(2)
#
# #전진
# drone.set_pitch(30)
# drone.move(2)
# drone.set_pitch(0)
#
# #하강
# drone.set_throttle(-25)
# drone.move(1)
#
# #전진
# drone.set_pitch(30)
# drone.move(2)
# drone.set_pitch(0)
#
# #상승
# drone.set_throttle(25)
# drone.move(1)
#
# #버저 5회 작동
# drone.drone_buzzer(Note.C4, 500)
# drone.drone_buzzer(Note.D4, 500)
# drone.drone_buzzer(Note.E4, 500)
# drone.drone_buzzer(Note.F4, 500)
# drone.drone_buzzer(Note.G4, 500)
#
# #왼쪽 으로 회전
# drone.set_yaw(-25)
# drone.move(1)
#
# #이동 하며 사각형 그리기
# drone.set_pitch(30)
# drone.move(2)
# drone.set_pitch(0)
#
# drone.set_roll(30)
# drone.move(2)
# drone.set_roll(0)
#
# drone.set_pitch(-30)
# drone.move(2)
# drone.set_pitch(0)
#
# drone.set_roll(-30)
# drone.move(2)
# drone.set_pitch(0)
#
# #버저 5회 작동
# drone.drone_buzzer(Note.C4, 500)
# drone.drone_buzzer(Note.D4, 500)
# drone.drone_buzzer(Note.E4, 500)
# drone.drone_buzzer(Note.F4, 500)
# drone.drone_buzzer(Note.G4, 500)
#
# #정수 읽고 저장하기
#
# #착륙 지점까지 전진하기
# drone.set_pitch(30)
# drone.move(2)
# drone.set_pitch(0)
#
# 드론 착륙
drone.land()

# 버저 5회 작동
# drone.drone_buzzer(Note.C4, 500)
# drone.drone_buzzer(Note.D4, 500)
# drone.drone_buzzer(Note.E4, 500)
# drone.drone_buzzer(Note.F4, 500)
# drone.drone_buzzer(Note.G4, 500)

# 드론 종료
drone.close()

# 드론 종료 시간 측정

# 드론 시작,종료,실행 시간 파일로 저장



"""
drone.land()

drone.close()
