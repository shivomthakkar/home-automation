

def connectToWifiAndUpdate():
    import time, machine, network, gc
    from app.secrets import Secrets
    time.sleep(1)
    print('Memory free', gc.mem_free())

    from app.ota_updater import OTAUpdater

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        secrets = Secrets()
        sta_if.active(True)
        sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    # otaUpdater = OTAUpdater('https://github.com/shivomthakkar/micropython-ota-updater', main_dir='app', secrets_file="secrets.py")
    token='aa517681738b4971cc55b7d9e8967780ff1f443b'
    otaUpdater = OTAUpdater('https://github.com/shivomthakkar/micropython-ota-updater', main_dir="app", headers={'Authorization': 'token {}'.format(token)})
    hasUpdated = otaUpdater.install_update_if_available()
    if hasUpdated:
        machine.reset()
    else:
        del(otaUpdater)
        gc.collect()

def startApp():
    import app.start


connectToWifiAndUpdate()
startApp()