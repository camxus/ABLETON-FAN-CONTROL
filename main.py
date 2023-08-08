import sys
import os
from pynput import keyboard


SET_FAN_SPEED=2000

def on_press(key):
    fan_speed = hex(SET_FAN_SPEED << 2).split("x")[1]
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k == "f9":  # keys of interest
        # self.keys.append(k)  # store it in global-like variable

        # set both fans to forced mode
        os.system(f'smc -k "FS! " -w 0003')
        # set fan speed
        os.system(f'smc -k F0Tg -w {fan_speed}')
        os.system(f'smc -k F1Tg -w {fan_speed}')

        print(f'Fan speed force set: {SET_FAN_SPEED} {fan_speed}')
        print('Key pressed: ' + k)

        return True

    if k in ["esc", "space"]:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable

        # set both fans to auto mode
        os.system(f'smc -k "FS! " -w 0000')
        print('Key pressed: ' + k)

        return True


def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()