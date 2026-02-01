from pywebostv.discovery import discover
from pywebostv.connection import WebOSClient
from pywebostv.controls import ApplicationControl, MediaControl, SystemControl
import time
import json

# IP found in the scan
target_ip = "192.168.0.11"

client = WebOSClient(target_ip)
client.connect()

# Check if we already have a store (we don't yet)
store = {}

# Start pairing
for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("PROMPTED: Please accept the connection on the TV screen.")
    elif status == WebOSClient.REGISTERED:
        print("REGISTERED: Connection successful!")
        print(json.dumps(store))
