from esp32_now_send import Send  
import machine
from time import sleep


sender = Send('<enter esp32 receiver board mac address here>')
button_pin = machine.Pin(15, machine.Pin.IN)
led_pin = machine.Pin(2, machine.Pin.OUT)
led_state = False

while True:
    sleep(0.3)
    button_state = button_pin.value()
    if button_state == 0:
        led_state = not led_state
        led_pin.value(led_state)
        if led_state:
            print('On')
            sender.send('65')
            sleep(5)
        else:
            print("Off")
            sender.send('100')
            sleep(5)
