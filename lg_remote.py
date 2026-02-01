import sys
from pywebostv.connection import WebOSClient
from pywebostv.controls import MediaControl, SystemControl, ApplicationControl, InputControl

# Configuration
target_ip = "192.168.0.11"
client_key = "25d472261604e7ee1ba8af700b353232"

client = WebOSClient(target_ip)
client.connect()
store = {"client_key": client_key}
for status in client.register(store):
    pass

system = SystemControl(client)
media = MediaControl(client)
app = ApplicationControl(client)
inp = InputControl(client)
inp.connect_input()

if len(sys.argv) < 2:
    print("Usage: python3 lg_remote.py <command> [value]")
    sys.exit(1)

cmd = sys.argv[1]

if cmd == "notify":
    system.notify(sys.argv[2])
elif cmd == "volup":
    media.volume_up()
elif cmd == "voldown":
    media.volume_down()
elif cmd == "mute":
    media.set_mute(True)
elif cmd == "unmute":
    media.set_mute(False)
elif cmd == "play":
    media.play()
elif cmd == "pause":
    media.pause()
elif cmd == "stop":
    media.stop()
elif cmd == "up":
    inp.up()
elif cmd == "down":
    inp.down()
elif cmd == "left":
    inp.left()
elif cmd == "right":
    inp.right()
elif cmd == "ok":
    inp.ok()
elif cmd == "back":
    inp.back()
elif cmd == "home":
    inp.home()
elif cmd == "type":
    inp.type(sys.argv[2])
elif cmd == "off":
    system.power_off()
elif cmd == "list_apps":
    apps = app.list_apps()
    for a in apps:
        print(f"{a.data}")
elif cmd == "launch":
    apps = app.list_apps()
    target = sys.argv[2].lower()
    for a in apps:
        title = a.data.get('title', '').lower()
        id = a.data.get('id', '').lower()
        if target in title or target in id:
            app.launch(a)
            print(f"Launched {title}")
            break
