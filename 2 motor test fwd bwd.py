from guizero import App, Text, PushButton
from gpiozero import Robot, LED
from time import sleep

motor = Robot(left=(4, 14),right=(17, 18))
motorSwitch = LED(27) 

app = App(title="GUI Development", layout="grid", height=600, width=800)
message = Text(app, text="Dual Motor Control Interface", grid=[4,0])

motorSpeedForward = 0
motorSpeedBackward = 0

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
    if button1.text=="Forward OFF" :
        motorSpeedForward = 1
        button1.text="Forward ON"
        print("motor stopped")
    elif button1.text=="Forward ON" :
        motorSpeedForward = 0
        button1.text="Forward OFF"
        print("motor forward")

def backward():
    global motorSpeedBackward
    motor.backward(speed=motorSpeedBackward)
    if button2.text=="Backward OFF" :
        motorSpeedBackward = 1
        button2.text="Backward ON"
        print("motor stopped")
    elif button2.text=="Backward ON" :
        motorSpeedBackward = 0
        button2.text="Backward OFF"
        print("motor backward")

Text(app, "Motor",grid=[2,1])
button0 = PushButton(app, command=toggleSwitch, text="Start", width=10,height=3, grid=[2,4])
button1 = PushButton(app, command=forward, text = "Forward ON", width=10,height=3, grid=[1,4])
button2 = PushButton(app, command=backward, text="Backward ON", width=10, height=3, grid=[3,4])

app.display()