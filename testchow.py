import keyboard
import time

print("Press 'q' to quit.")
while True:
    if keyboard.is_pressed('q'):
        print("Quitting...")
        break
    time.sleep(0.1)  # Short delay to avoid busy-waiting