import network, espnow

class Receive:
    def __init__(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        self.esp_now = espnow.ESPNow()
        self.esp_now.active(True)

    def receive(self):
        if self.esp_now.any():
            _, msg = self.esp_now.recv()
            return int(msg)
