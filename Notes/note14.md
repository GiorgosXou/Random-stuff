`2026-04-14 07:12:25 PM`


# (Arch) Linux Setup
1. Install libjaylink

```
sudo pacman -S libjaylink
```

2. Add [rules for WCH-Link programmer][1], to be recognised when connected via USB:

```
sudo nano /etc/udev/rules.d/99-wch.rules
```

```
# WinChipHead CHxxx series in programming mode
SUBSYSTEM=="usb", ATTR{idVendor}="1a86", ATTR{idProduct}=="8010" MODE="0666"
SUBSYSTEM=="usb", ATTR{idVendor}="4348", ATTR{idProduct}=="55e0" MODE="0666"
SUBSYSTEM=="usb", ATTR{idVendor}="1a86", ATTR{idProduct}=="8012" MODE="0666"
```

3. `lsusb` should show something similar to:

```
...
Bus 001 Device 054: ID 1a86:8010 QinHeng Electronics WCH-Link
...
```


# ~Arduino~ (not recommended)

1. Go to *"File>Preferences>Additional Boards Manager URLs"* and add:
```
https://github.com/openwch/board_manager_files/raw/main/package_ch32v_index.json
```

2. Go to Board Manager and install `CH32 MCU EVT Boards by WCH`


# Bare-metal
Follow the instruction here: https://github.com/cnlohr/ch32fun


# Troubleshooting

1. If stuck in debug mode or anything else simply try [wlink-iap][2] *(it solved my issues)*
2. If uploading shows `Error:  ...check your physical link connection` check the connector. The cable that came with my WCH-Link-programmer for some reason it had V3 SWDIO GND while my CH32V003-Board had V3 GND SWDIO *(which took me a while to see)*


[2]: https://github.com/cjacker/wlink-iap
[1]: https://pio-ch32v.readthedocs.io/en/latest/installation.html#linux-udev-rules
