from machine import Pin, reset
from time import sleep, time
from onewire import OneWire
from ds18x20 import DS18X20
from esp32_now_receive import Receive

p2 = Pin(2, Pin.OUT)
p32 = Pin(32, Pin.OUT)
ds4 = DS18X20(OneWire(Pin(4)))
command = Receive()

p2.off()
p32.off()
temp_threshold = None  # Initialize to None
min_active_time = 300  # Minimum active time in seconds (5 minutes)
last_activation_time = 0  # Time when pins were last activated

while True:
    try:
        current_time = time()
        if command.esp_now.any():  # Check for new threshold command
            new_threshold = command.receive()
            if new_threshold is not None:
                temp_threshold = new_threshold
                # Check if new threshold requires immediate action
                ds4.convert_temp()
                rom = ds4.scan()[0]
                current_temp = ds4.read_temp(rom) * 1.8 + 32
                if current_temp <= new_threshold and current_time - last_activation_time < min_active_time:
                    p2.off()
                    p32.off()

        ds4.convert_temp()
        sleep(1)  # Allow time for temperature conversion
        rom = ds4.scan()[0]
        temp = ds4.read_temp(rom) * 1.8 + 32
        print(f"Temperature: {temp} F")

        if temp_threshold is not None:
            if temp > temp_threshold:
                if not p2.value() or not p32.value():
                    p2.on()
                    p32.on()
                    last_activation_time = current_time
            elif current_time - last_activation_time >= min_active_time and temp <= temp_threshold:
                p2.off()
                p32.off()

        sleep(4)  # Sleep to make up the total to 5 seconds
    except Exception as e:
        print(e)
        p2.off()
        p32.off()
        reset()
