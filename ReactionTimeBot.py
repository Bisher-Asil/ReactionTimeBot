from pyautogui import *
import pyautogui 
import time
import keyboard

## This code is written to get the best reaction time on https://www.justpark.com/creative/reaction-time-test/

## The numbers below are manually aquired (wont work on different screens)
## Center: 870 763
## Gray: 150


## This is used to make sure we dont skip the results
i =0

def press():
    keyboard.press_and_release("space")
    print("Pressed")
try:
    while keyboard.is_pressed('q') == False:
        if pyautogui.pixel(870,763)[0] != 150 and i < 1:
            press()
            i+=1  
except :
    pass 