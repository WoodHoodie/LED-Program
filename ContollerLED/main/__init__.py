import opc
import time
import sys
from urllib.request import localhost


led_colours= [(0 ,0 ,0)] * 360
client= opc.Client("localhost:7890")

client.put_pixels(led_colours, 0)
