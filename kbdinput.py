from gpiozero import Robot, LED
from keyboard._keyboard_event import KEY_DOWN, KEY_UP
import keyboard
from signal import pause

motor = Robot(left=(17, 18), right=(4, 14))
motorSwitch = LED(27)
motorSwitch.on()
motorSpeed = 1

def forward():
    motor.forward(speed=motorSpeed)

def reverse():
    motor.backward(speed=motorSpeed)


def right():
    motor.right(speed=motorSpeed)

def left():
    motor.left(speed=motorSpeed)

def stop_motors():
    motor.stop()

def on_action(event):
    if event.event_type == KEY_DOWN:
        on_press(event.name)
    
    elif event.event_type == KEY_UP:
        on_release(event.name)

def on_press(key) :
    if key == 'w' :
        forward()
    if key == 's' :
        reverse()
    if key == 'd' :
        right()
    if key == 'a' :
        left()

def on_release(key) :
    if key == 'w' or 's' or 'a' or 'd' :
        stop_motors()

keyboard.hook(lambda e: on_action(e))    
    
pause()