import wmi
import time
from allthingstalk import Client, Device, NumberAsset


class Laptop(Device):
    CPU_CORE_4 = NumberAsset(unit='°C')
    CPU_CORE_3 = NumberAsset(unit='°C')
    CPU_CORE_2 = NumberAsset(unit='°C')
    CPU_CORE_1 = NumberAsset(unit='°C')


# reading the temperatures corresponding to the 4 CPU cores
def get_temps():
    temp_data = [0, 0, 0, 0]
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    for sensor in temperature_infos:
        if sensor.SensorType == u'Temperature':
            if sensor.Name == "CPU Core #1":
                temp_data[0] = sensor.Value
            elif sensor.Name == "CPU Core #2":
                temp_data[1] = sensor.Value
            elif sensor.Name == "CPU Core #3":
                temp_data[2] = sensor.Value
            elif sensor.Name == "CPU Core #4":
                temp_data[3] = sensor.Value
    return temp_data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = Client('maker:4UsknYiJWyGFG0lqFzHsZyf5wfRiWzpDcF1ccrc0')
    laptop = Laptop(client=client, id='UKdCN9nzmqXmRTtsFXbikGj4')
    while True:
        data = get_temps()
        laptop.CPU_CORE_1 = data[0]
        laptop.CPU_CORE_2 = data[1]
        laptop.CPU_CORE_3 = data[2]
        laptop.CPU_CORE_4 = data[3]

