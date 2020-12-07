from allthingstalk import Client, Device, NumberAsset, BooleanAsset, Asset
import time


class Laptop(Device):
    CPU_CORE_4 = NumberAsset(unit='°C')
    CPU_CORE_3 = NumberAsset(unit='°C')
    CPU_CORE_2 = NumberAsset(unit='°C')
    CPU_CORE_1 = NumberAsset(unit='°C')
    ALERT_CORE_1 = BooleanAsset(kind=Asset.VIRTUAL)
    ALERT_CORE_2 = BooleanAsset(kind=Asset.VIRTUAL)
    ALERT_CORE_3 = BooleanAsset(kind=Asset.VIRTUAL)
    ALERT_CORE_4 = BooleanAsset(kind=Asset.VIRTUAL)


@Laptop.feed.CPU_CORE_1
def on_reset(device, value, at):
    print('CPU_CORE_1: %d at %s' % (value, at))
    device.ALERT_CORE_1 = value >= 70.0


@Laptop.feed.CPU_CORE_2
def on_reset(device, value, at):
    print('CPU_CORE_2: %d at %s' % (value, at))
    device.ALERT_CORE_2 = value >= 70.0


@Laptop.feed.CPU_CORE_3
def on_reset(device, value, at):
    print('CPU_CORE_3: %d at %s' % (value, at))
    device.ALERT_CORE_3 = value >= 70.0


@Laptop.feed.CPU_CORE_4
def on_reset(device, value, at):
    print('CPU_CORE_4: %d at %s\n' % (value, at))
    device.ALERT_CORE_4 = value >= 70.0


if __name__ == '__main__':
    client = Client("maker:4Nt85ldXaPeOW1VeVtm1Uc9dpj2OHYRyzavIzCn1")
    laptop = Laptop(client=client, id="UKdCN9nzmqXmRTtsFXbikGj4")
    while True:
        time.sleep(5)
