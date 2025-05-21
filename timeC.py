from datetime import datetime
from time import sleep

# 현재 시간 가져오기


def timestart():
    st = datetime.now()
    print("시작 시간:", st)
    return st


def timeend(st):
    et = datetime.now()
    print("종료 시간:", et)

    rt = et - st

    print("실행 시간:", rt)

    f = open("./Time Print.txt", "w")

    f.write(
        "start_time : "
        + str(st)
        + "\n"
        + "end_time : "
        + str(et)
        + "\n"
        + "run_time : "
        + str(rt)
    )

    f.close()
