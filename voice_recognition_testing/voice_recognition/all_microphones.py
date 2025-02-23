import pyaudio

p = pyaudio.PyAudio()

info = p.get_host_api_info_by_index(0)
device_count = info.get('deviceCount')

print("Verfügbare Mikrofone:")

for i in range(0, device_count):
    device_info = p.get_device_info_by_index(i)
    if device_info.get('maxInputChannels') > 0:  
        print(f"ID: {i}, Name: {device_info.get('name')}")


p.terminate()
