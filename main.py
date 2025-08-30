from winotify import Notification, audio
import psutil

import time

showed_20 = False
showed_80 = False
showed_100 = False

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged

    if percent <= 20 and not plugged and not showed_20:
        toast = Notification(app_id="Pyttery",
                             title="Battery",
                             msg="Battery level is 20%")
        toast.set_audio(audio.Default, loop=False)
        toast.show()
        showed_20 = True
    elif percent >= 80 and plugged and not showed_80:
        toast = Notification(app_id="Pyttery",
                             title="Battery",
                             msg="Battery level is 80%")
        toast.set_audio(audio.Default, loop=False)
        toast.show()
        showed_80 = True
    elif percent == 100 and plugged and not showed_100:
        toast = Notification(app_id="Pyttery",
                             title="Battery",
                             msg="Battery level is 100%")
        toast.set_audio(audio.Default, loop=False)
        toast.show()
        showed_100 = True

    if percent > 20:
        showed_20 = False
    if percent < 80:
        showed_80 = False
    if percent < 100:
        showed_100 = False

    time.sleep(2)
