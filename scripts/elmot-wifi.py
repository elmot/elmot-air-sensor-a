import network, localsecrets
nic=network.WLAN(network.STA_IF)
nic.active(True)
nic.connect(localsecrets.SSID,localsecrets.PASSWORD)