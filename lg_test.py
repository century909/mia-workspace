import json
from pywebostv.connection import WebOSClient
from pywebostv.controls import MediaControl, SystemControl, ApplicationControl

target_ip = "192.168.0.11"
client_key = "25d472261604e7ee1ba8af700b353232"

client = WebOSClient(target_ip)
client.connect()

store = {"client_key": client_key}
for status in client.register(store):
    if status == WebOSClient.REGISTERED:
        print("Registration confirmed")

system = SystemControl(client)
system.notify("¡Mia está conectada! 👾")
print("Notification sent")
