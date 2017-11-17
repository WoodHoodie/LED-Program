import opc
import time
import sys
import _thread
from urllib.request import localhost


def animation_loop(i):
    while run:
        for led in enumerate(led_colours):
            if (led[0]< 60):
                r= 255
                g= 0
                b= 0
            elif (led[0]>= 60 and led[0]< 120):
                r= 255
                g= 150
                b= 0
            elif (led[0]>= 120 and led[0]< 180):
                r= 255
                g= 255
                b= 0
            elif (led[0]>= 180 and led[0]< 240):
                r= 0
                g= 255
                b= 0
            elif (led[0]>= 240 and led[0]< 300):
                r= 100
                g= 100
                b= 255
            else:
                r= 220
                g= 100
                b= 255
            led_colours[led[0]]= (r, g, b)
        client.put_pixels(led_colours, 0)
        time.sleep(0.2)

        

led_colours= [(255 ,0 ,0)] * 360
lead_leds= [0, 60, 120, 180, 240, 300]
client= opc.Client("localhost:7890")
run= True
_thread.start_new_thread(animation_loop, (0,))
input("Press any key to exit...")
run= False
clear_led= [(0, 0, 0)]* 360
client.put_pixels(clear_led)
sys.exit(0)