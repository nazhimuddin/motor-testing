from gpiozero import Robot, LED, Button
from signal import pause

motor = Robot(left=(17, 18), right=(4, 14))
motorSwitch = LED(27)

motorSwitch.on()
motorSpeedForward =0
motorSpeedReverse=0
motorSpeedRight=0
motorSpeedLeft =0

def forward():
    global motorSpeedForward
    motor.forward(speed=motorSpeedForward)
    motorSpeedForward = 1

def reverse():
    global motorSpeedReverse
    motor.backward(speed=motorSpeedReverse)
    motorSpeedReverse = 1

def right():
    global motorSpeedRight
    motor.right(speed=motorSpeedRight)
    motorSpeedRight = 1

def left():
    global motorSpeedLeft
    motor.left(speed=motorSpeedLeft)
    motorSpeedLeft = 1

def stop_movement():
    motor.stop()

button1 = Button(26)
button2 = Button(19)
button3 = Button(6)
button4 = Button(13)

button1.when_pressed= forward
button1.when_released = stop_movement

button2.when_pressed = reverse
button2.when_released = stop_movement

button3.when_pressed = right
button3.when_released = stop_movement

button4.when_pressed = left
button4.when_released = stop_movement

pause()