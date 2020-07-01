#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# word layout for the overlay see the .svg file
#   01234567
# 0 STWENTYS
# 1 FIVEHALF
# 2 FIFTEEN*
# 3 PASTO***
# 4 FIVEIGHT
# 5 SIXTHREE
# 6 TWELEVEN
# 7 FOURNINE
#

import datetime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas

def getadd(minute):  # make an additive of 4 or less to add to the five minutes displayed
    while 5:
        if minute > 5:
            minute -= 5
        else:
            break
    additive = minute
    return additive

def face(hour, minute):
    # setup the device
    serial = spi(port=0, device=1, gpio=noop())
    # originally I programed this on a CrowPi and had to rotate=3 to make it look correct adjust as required (0-3)
    device = max7219(serial, cascaded=1,  block_orientation=0, rotate=3)
    device.contrast(1 * 16) # 0 - 15 * 16 for brightness
    
    # draw the face according to the current time
    # to the new hour or passing the old hour
    with canvas(device) as draw:
        if minute > 0 and minute < 31: #past
            # print('past')
            draw.point((0,3), fill=1)
            draw.point((1,3), fill=1)
            draw.point((2,3), fill=1)
            draw.point((3,3), fill=1)
        if minute > 30 and minute < 60:  # to
            # print('to')
            draw.point((3,3), fill=1)
            draw.point((4,3), fill=1)
            hour += 1
        if hour > 12:
            hour -= 12
            # print(hour)
        # display five minute increments for minutes
        if minute > 4 and minute < 10  or minute < 30 and minute > 24 or minute < 36 and \
               minute > 30 or minute > 50 and minute < 56:
            draw.point((0,1), fill=1)
            draw.point((1,1), fill=1)
            draw.point((2,1), fill=1)
            draw.point((3,1), fill=1)
            # print('five')
        if minute < 15 and minute > 9 or minute < 51 and minute > 45:
            draw.point((1,0), fill=1)
            draw.point((3,0), fill=1)
            draw.point((4,0), fill=1)
            # print('ten')
        if minute < 20 and minute > 14 or minute < 46 and minute > 40:
            draw.point((0,2), fill=1)
            draw.point((1,2), fill=1)
            draw.point((2,2), fill=1)
            draw.point((3,2), fill=1)
            draw.point((4,2), fill=1)
            draw.point((5,2), fill=1)
            draw.point((6,2), fill=1)
            # print('fifteen')
        if minute < 30 and minute > 19 or minute < 41 and minute > 30:
            draw.point((1,0), fill=1)
            draw.point((2,0), fill=1)
            draw.point((3,0), fill=1)
            draw.point((4,0), fill=1)
            draw.point((5,0), fill=1)
            draw.point((6,0), fill=1)
            # print('twenty')
        if minute < 31 and minute > 29:
            draw.point((4,1), fill=1)
            draw.point((5,1), fill=1)
            draw.point((6,1), fill=1)
            draw.point((7,1), fill=1)
            # print('half')
        # display the hour in munbers
        if hour == 1:  # one
            draw.point((1,7), fill=1)
            draw.point((4,7), fill=1)
            draw.point((7,7), fill=1)
        if hour == 2:  # two
            draw.point((0,6), fill=1)
            draw.point((1,6), fill=1)
            draw.point((1,7), fill=1)
        if hour == 3:  # three
            draw.point((3,5), fill=1)
            draw.point((4,5), fill=1)
            draw.point((5,5), fill=1)
            draw.point((6,5), fill=1)
            draw.point((7,5), fill=1)
        if hour == 4:  # four
            draw.point((0,7), fill=1)
            draw.point((1,7), fill=1)
            draw.point((2,7), fill=1)
            draw.point((3,7), fill=1)
        if hour == 5:  # five
            draw.point((0,4), fill=1)
            draw.point((1,4), fill=1)
            draw.point((2,4), fill=1)
            draw.point((3,4), fill=1)
        if hour == 6:  # six
            draw.point((0,5), fill=1)
            draw.point((1,5), fill=1)
            draw.point((2,5), fill=1)
        if hour == 7:  # seven
            draw.point((0,5), fill=1)
            draw.point((4,6), fill=1)
            draw.point((5,6), fill=1)
            draw.point((6,6), fill=1)
            draw.point((7,6), fill=1)
        if hour == 8:  # eight
            draw.point((3,4), fill=1)
            draw.point((4,4), fill=1)
            draw.point((5,4), fill=1)
            draw.point((6,4), fill=1)
            draw.point((7,4), fill=1)
        if hour == 9:  # nine
            draw.point((4,7), fill=1)
            draw.point((5,7), fill=1)
            draw.point((6,7), fill=1)
            draw.point((7,7), fill=1)
        if hour == 10:  # ten
            draw.point((7,4), fill=1)
            draw.point((7,5), fill=1)
            draw.point((7,6), fill=1)
        if hour == 11:  # eleven
            draw.point((2,6), fill=1)
            draw.point((3,6), fill=1)
            draw.point((4,6), fill=1)
            draw.point((5,6), fill=1)
            draw.point((6,6), fill=1)
            draw.point((7,6), fill=1)
        if hour == 12:  # twelve
            draw.point((0,6), fill=1)
            draw.point((1,6), fill=1)
            draw.point((2,6), fill=1)
            draw.point((3,6), fill=1)
            draw.point((5,6), fill=1)
            draw.point((6,6), fill=1)

        #fine tune the minutes
        additive = getadd(minute)
        if additive == 1:
            if minute < 31:
                draw.point((5,3), fill=1)
            elif minute > 30:
                draw.point((5,3), fill=1)
                draw.point((6,3), fill=1)
                draw.point((7,3), fill=1)
                draw.point((7,2), fill=1)
        if additive == 2:
            if minute < 31:
                draw.point((5,3), fill=1)
                draw.point((6,3), fill=1)
            elif minute > 30:
                draw.point((5,3), fill=1)
                draw.point((6,3), fill=1)
                draw.point((7,3), fill=1)
        if additive == 3:
            if minute < 31:
                draw.point((5,3), fill=1)
                draw.point((6,3), fill=1)
                draw.point((7,3), fill=1)
            elif minute > 30:
                draw.point((5,3), fill=1)
                draw.point((6,3), fill=1)
        if additive == 4:
            if minute < 31:
                draw.point((5,3), fill=1)
                draw.point((6,3), fill=1)
                draw.point((7,3), fill=1)
                draw.point((7,2), fill=1)
            elif minute > 30:
                draw.point((5,3), fill=1)
        newminute = minute + 1
        if newminute == 60:
            newminute = 0
        return newminute

def main():
    # draw the first clock face
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    newminute = face(hour, minute)
    
    while True:
        # if it a new minute then re-draw the face
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        if minute == newminute:
            newminute = face(hour,minute)
        else:
            pass
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # clear the matrix for exit
        serial = spi(port=0, device=1, gpio=noop())
        device = max7219(serial, cascaded=1,  block_orientation=0, rotate=3)
        device.cleanup()
        pass
