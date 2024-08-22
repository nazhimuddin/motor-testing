
from guizero import App, Text, PushButton
from gpiozero import Robot, LED
from time import sleep

motor = Robot(left=(17, 18),right=(4, 14))
motorSwitch = LED(27) 

app = App(title="GUI Development", layout="grid", height=600, width=800)
message = Text(app, text="Dual Motor Control Interface", grid=[4,0])

motorSpeedForward = 0
motorSpeedReverse = 0
motorSpeedRight = 0
motorSpeedLeft = 0
motorSpeedAll = 0

def toggleSwitch():
    if button0.text=="Start":
       motorSwitch.on()
       button0.text="Stop"
    elif button0.text == "Stop":
         motorSwitch.off()
         button0.text = "Start"

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

def buttonrelease():
    global motorSpeedAll
    motor.all(speed=motorSpeedAll)
    motorSpeedAll =0



Text (app, "Motor",grid=[2,1])
button0 = PushButton(app, command=toggleSwitch, text="Start", width=10,height=3, grid=[2,4])
button1 = PushButton(app, command=forward, text = "Forward", width=10,height=3, grid=[2,3])
button2 = PushButton(app, command=reverse, text="Backward", width=10, height=3, grid=[2,5])
button3 = PushButton(app, command=right, text="Right", width=10, height=3, grid=[1,4])
button4 = PushButton(app, command=left, text="Left", width=10, height=3, grid=[3,4])

if button1 == 1:
    forward()

if button2 == 1:
    reverse()

if button3 == 1:
    right()

if button4 == 1:
    left()
  
app.display()