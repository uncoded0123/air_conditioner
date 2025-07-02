def v1():
    import time, network
    station = network.WLAN(network.STA_IF)
    station.active(True)
    while station.isconnected() == False:
        station.connect("username", "password")
        time.sleep(1)
    print("Connected!")

def v2():
    import time, network
    station = network.WLAN(network.STA_IF)
    station.active(True)
    time.sleep(1)
    while station.isconnected() == False:
        station.connect("username", "password")
        time.sleep(1)
    print("Connected!")

def v3():
    import time, network
    station = network.WLAN(network.STA_IF)
    station.active(True)
    time.sleep(5)  # Increase sleep time
    while not station.isconnected():
        station.connect("username", "password")
        time.sleep(5)  # Increase sleep time
    print("Connected!")

def v4():
    import time, network, machine

    wdt = machine.WDT(timeout=30000)  # Watchdog timer for 30 seconds

    station = network.WLAN(network.STA_IF)
    station.active(True)
    time.sleep(5)

    if not station.isconnected():
        station.connect("username", "password")
        start = time.time()
        while not station.isconnected() and time.time() - start < 30:
            time.sleep(1)
            wdt.feed()  # Reset the watchdog timer

    print("Connected!" if station.isconnected() else "Failed to connect")
    
v4()
