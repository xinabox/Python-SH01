[![GitHub Issues](https://img.shields.io/github/issues/xinabox/Python-SH01.svg)](https://github.com/xinabox/Python-SH01/issues)
![GitHub Commit](https://img.shields.io/github/last-commit/xinabox/Python-SH01)
![Maintained](https://img.shields.io/maintenance/yes/2020)
![Build status badge](https://github.com/xinabox/Python-SH01/workflows/Python/badge.svg)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

# Python-SH01

The SH01 xChip is a multiple channel capacitive touch sensor controller. It is based on the CAP1296 manufactured by Microchip. Each sensor input is calibrated to compensate for system parasitic capacitance and automatically recalibrated to compensate for gradual environmental changes. In addition, the CAP1296 can be configured to detect proximity on one or more channels with an optional signal guard to reduce noise sensitivity. The CAP1296 includes Multiple Pattern Touch recognition that allows the user to select a specific set of buttons to be touched simultaneously. If this pattern is detected, a status bit is set and an interrupt is generated.

# Usage

## Mu-editor
Download [Mu-editor](https://github.com/xinabox/mu-editor/releases/tag/v1.1.0a2)

### CW01 and CW02
- Use [XinaBoxUploader](https://github.com/xinabox/XinaBoxUploader/releases/latest) and flash MicroPython to the CW01/CW02.
- Download Python packages from the REPL with the following code:
    ```python
    import network
    import upip
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("ssid", "password")
    upip.install("xinabox-SH01")
    ```

### CC03, CS11 and CW03
- Download the .UF2 file for CC03/CS11/CW03 [CircuitPython](https://circuitpython.org/board/xinabox_cs11/) and flash it to the board.
- TO DO

### MicroBit
- TO DO

## Raspberry Pi

Requires Python 3
```
pip3 install xinabox-SH01
```

# Example
```python
from xCore import xCore
from xSH01 import xSH01

# SH01 instance
SH01 = xSH01()

# configure SH01
SH01.init()

while True:
    button = SH01.touched()         # return which button is pressed
    if button  == 'square':         # square touched
        print('SQUARE TOUCHED')
    elif button == 'triangle':      # triangle touched
        print('TRIANGLE TOUCHED')
    elif button == 'circle':        # circle touched
        print('CIRCLE TOUCHED')
    elif button == 'cross':         # cross touched
        print('CROSS TOUCHED')

    xCore.sleep(100)
```