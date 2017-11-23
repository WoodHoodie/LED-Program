import opc
import time
import sys
import _thread
from urllib.request import localhost

def rainbow_wave(led):
    global led_colours
    global lead_leds
    #sets red line
    if (led[0]>= lead_leds[0] and (led[0]< lead_leds[1] or (led[0]>= 300 and led[0]< 360-lead_leds[1]))):
        r= 255
        g= 0
        b= 0
    #sets orange
    elif (led[0]>= lead_leds[1] and (led[0]< lead_leds[2] or (led[0]>= 300 and led[0]< 360-lead_leds[2]))):
        r= 255
        g= 150
        b= 0
    #sets yellow
    elif (led[0]>= lead_leds[2] and (led[0]< lead_leds[3] or (led[0]>= 300 and led[0]< 360-lead_leds[3]))):
        r= 255
        g= 255
        b= 0
    #green
    elif (led[0]>= lead_leds[3] and (led[0]< lead_leds[4] or (led[0]>= 300 and led[0]< 360-lead_leds[4]))):
        r= 0
        g= 255
        b= 0
    #blue
    elif (led[0]>= lead_leds[4] and (led[0]< lead_leds[5] or (led[0]>= 300 and led[0]< 360-lead_leds[5]))):
        r= 100
        g= 100
        b= 255
    #violet
    else:
        r= 220
        g= 100
        b= 255
    led_colours[led[0]]= (r, g, b)
    #moves the rows along once all LEDs changed
    if (led[0]>= len(led_colours)- 1):
        for lead in enumerate(lead_leds):
            new_lead= lead[1]- 60
            if (new_lead< 0):
                new_lead= 300
            lead_leds[lead[0]]= new_lead
    
def rainbow_pulse(led):
    global led_colours
    global lead_leds
    
    r = led[1][0]
    g = led[1][1]
    b = led[1][2]
    
    if (led[0] in lead_leds):
        r = 0
        g = 0
        b = 255
    
    elif (b > 0 and r==0):
       r = 0
       g+= 13
       b-= 13
    elif (g > 0 and b==0):
        r+= 13
        g-= 13
        b = 0
    elif (r > 0 and g==0):
        r-= 13
        g = 0
        b+= 13
    else:
        r = 0
        g = 0
        b = 0
    if r > 255:
        r = 255
    if r < 0:
        r = 0 
    if g > 255:
        g = 255
    if g < 0:
        g = 0 
    if b > 255:
        b = 255
    if b < 0:
        b = 0
    if (led[0]>=len(led_colours) -1):
        for lead in enumerate(lead_leds):
            new_lead = lead[1] +1
            lead_leds[lead[0]]= new_lead
    if(lead_leds[0]>= 60):
        lead_leds = [0, 60, 120, 180, 240, 300]
    led_colours[led[0]]= (r, g, b)
    
def mono_pulse(led):
    global led_colours
    global lead_leds
    
    r = led[1][0]
    g = led[1][1]
    b = led[1][2]
    
    if (led[0] in lead_leds):
        r = 255
        g = 255
        b = 255
    
    elif (b > 0):
       r-= 5
       g-= 5
       b-= 5
    
    else:
        r = 0
        g = 0
        b = 0
    if r > 255:
        r = 255
    if r < 0:
        r = 0 
    if g > 255:
        g = 255
    if g < 0:
        g = 0 
    if b > 255:
        b = 255
    if b < 0:
        b = 0
    if (led[0]>=len(led_colours) -1):
        for lead in enumerate(lead_leds):
            new_lead = lead[1] +1
            lead_leds[lead[0]]= new_lead
    if(lead_leds[0]>= 60):
        lead_leds = [0, 60, 120, 180, 240, 300]
    led_colours[led[0]]= (r, g, b)
    
def mono_wave(led):
    global led_colours
    global lead_leds
  
    if (led[0]>= lead_leds[0] and (led[0]< lead_leds[1] or (led[0]>= 300 and led[0]< 360-lead_leds[1]))):
        r= 255
        g= 255
        b= 255
    
    elif (led[0]>= lead_leds[1] and (led[0]< lead_leds[2] or (led[0]>= 300 and led[0]< 360-lead_leds[2]))):
        r= 200
        g= 200
        b= 200
  
    elif (led[0]>= lead_leds[2] and (led[0]< lead_leds[3] or (led[0]>= 300 and led[0]< 360-lead_leds[3]))):
        r= 150
        g= 150
        b= 150
  
    elif (led[0]>= lead_leds[3] and (led[0]< lead_leds[4] or (led[0]>= 300 and led[0]< 360-lead_leds[4]))):
        r= 100
        g= 100
        b= 100
  
    elif (led[0]>= lead_leds[4] and (led[0]< lead_leds[5] or (led[0]>= 300 and led[0]< 360-lead_leds[5]))):
        r= 50
        g= 50
        b= 50
   
    else:
        r= 0
        g= 0
        b= 0
    led_colours[led[0]]= (r, g, b)
    #moves the rows along once all LEDs changed
    if (led[0]>= len(led_colours)- 1):
        for lead in enumerate(lead_leds):
            new_lead= lead[1]- 60
            if (new_lead< 0):
                new_lead= 300
            lead_leds[lead[0]]= new_lead
    
        
def animation_loop(i):
    #simple loop with frame pause
    while run:
        for led in enumerate(led_colours):
            mono_wave(led)
        client.put_pixels(led_colours, 0)
        time.sleep(0.2)

        
        
#Program runs from here
led_colours= [(0 ,0 ,0)] * 360
lead_leds= [0, 60, 120, 180, 240, 300]

#Local simulation client
client= opc.Client("localhost:7890")

#fadecandy client
#client= opc.Client("192.168.2.1:7890")

#start animation loop
run= True
_thread.start_new_thread(animation_loop, (0,))

#cleanup and exit on keypress
input("Press any key to exit...")
run= False
clear_led= [(0, 0, 0)]* 360
client.put_pixels(clear_led)
print("Program closed successfully!")
sys.exit(0)