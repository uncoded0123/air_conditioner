def internet():
    import connect
    import send_receive
    from time import sleep
    from machine import Pin
        
    p2 = Pin(2, Pin.OUT)

    while True:
        sleep(1)
        a = send_receive.receive()
        print(a)
        if 'on' in a.lower():
            p2.on()
        else:
            p2.off()
            
def esp32_now():
    import network
    import espnow
    from time import sleep
    from machine import Pin

    # Initialize Wi-Fi in STA mode
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    sleep(3)
    wlan.active(True)

    # Initialize ESP-NOW
    e = espnow.ESPNow()
    e.active(True)

    # Setup GPIO pin for LED
    led = Pin(2, Pin.OUT)

    def handle_message(msg):
        if msg == b'LED ON':
            led.value(1)
        elif msg == b'LED OFF':
            led.value(0)

    # Main loop to receive messages
    while True:
        host, msg = e.recv()
        if msg:
            handle_message(msg)


def timer():
    from machine import Pin, reset
    from time import sleep
    
    d2 = Pin(2, Pin.OUT)
    # electric 600W when compressor is on
    while True:
        try:
            min_on = 45
            min_off = 60
            sleep(1)
            d2.on()
            sleep(min_on * 60)
            d2.off()
            sleep(min_off * 60)
        except:
            sleep(5)
            reset()

#internet()
#esp32_now()
timer()
