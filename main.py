import sys
import os
import struct
from pynput import keyboard


SET_FAN_SPEED=2000

def on_press(key):
    fan_speed = bytearray(struct.pack('f', SET_FAN_SPEED)).hex()
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k == "f9":  # keys of interest
        # self.keys.append(k)  # store it in global-like variable

        # set both fans to forced mode
        os.system(f'smc -k "F0Md " -w 01')
        os.system(f'smc -k "F1Md " -w 01')
        # set fan speed
        # print(f'smc -k F0Tg -w {fan_speed}')
        os.system(f'smc -k F0Tg -w {fan_speed}')
        # print(f'smc -k F1Tg -w {fan_speed}')
        os.system(f'smc -k F1Tg -w {fan_speed}')

        print(f'Fan speed force set: {SET_FAN_SPEED} {fan_speed}')
        print('Key pressed: ' + k)

        return True

    if k in ["esc", "space"]:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable

        # set both fans to auto mode
        os.system(f'smc -k "F0Md " -w 00')
        os.system(f'smc -k "F1Md " -w 00')
        print('Key pressed: ' + k)

        return True


def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()