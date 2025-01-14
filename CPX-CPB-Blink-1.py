# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
bobs_button_B = digitalio.DigitalInOut(board.Button_B)
bobs_button_B.direction = digitalio.Direction.INPUT
bobs_button_B.pull = digitalio.Pull.DOWN

def main():
    print("Hello World")
    while True:
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)
    while True:
        led.value = bobs_button_B.value
        print(bobs_button_b.value)
        time.sleep(.2)
    print("Button_B Input/Output Example")
    print("Push Button_B (Right Button)")
main()
