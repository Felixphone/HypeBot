import json
import time

loop=1
trig_onoff=1

while loop==1:
    with open("data.json", "r") as f:
        data = json.load(f)
    trig_stat_fetch=(data["hype_onoff"])

    if trig_stat_fetch == 1:
        trig_onoff=1
        print("off")

    elif trig_stat_fetch == 0:
        trig_onoff=0

        print(trig_onoff)
        print("___________")

    else:
        print("err")

    time.sleep(0.1)
