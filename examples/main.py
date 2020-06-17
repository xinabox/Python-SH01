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