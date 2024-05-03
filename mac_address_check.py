# Run this on the esp32 receiver board to find its mac address, then type that address in esp32 controller board where it says
def mac_address_check():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    return ':'.join('{:02x}'.format(b) for b in wlan.config('mac'))
print(mac_address_check())
