import json
from pywebostv.connection import WebOSClient
from pywebostv.controls import MediaControl, SystemControl, ApplicationControl

target_ip = "192.168.0.11"
client_key = "25d472261604e7ee1ba8af700b353232"

client = WebOSClient(target_ip)
client.connect()
client.register({"client_key": client_key})

system = SystemControl(client)
media = MediaControl(client)
app = ApplicationControl(client)

# Mostrar un mensaje en pantalla para confirmar
system.notify("¡Mia está conectada! 👾")
