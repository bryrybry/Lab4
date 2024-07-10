import time
from time import sleep
from hal import hal_input_switch as switch
from hal import hal_led as led

led.init()
switch.init()

def main():
    cooldown = False
    while(True):
        if switch.read_slide_switch() == 1: # left
            blink(5, 0)
            cooldown = False
        else: # right
            if cooldown == False:    
                blink(10, 5)
            cooldown = True

def blink(freq, duration):
    if duration == 0:
        loopCount = 1
    else:
        loopCount = duration * freq
    for i in range(loopCount):
        led.set_output(0, 1)
        time.sleep(0.5/freq)
        led.set_output(0, 0)
        time.sleep(0.5/freq)

if __name__ == "__main__":
    main()
