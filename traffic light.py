from gpiozero import LED
import time
redLed = LED(2)
yellowLed = LED(3)
greenLed = LED(18)
lr = LED(17)
lg = LED(27)
lb = LED(22)
rr = LED(5)
rg = LED(6)
rb = LED(13)

def stop_light(_stop_light):
    print(_stop_light)

def traffic(traffic_light):
    if(traffic_light['redLed']) == 1:
        redLed.on()
    else:
        redLed.off()
    if(traffic_light['yellowLed']) == 1:
        yellowLed.on()
    else:
        yellowLed.off()
    if(traffic_light['greenLed']) == 1:
        greenLed.on()
    else:
        greenLed.off()
    print(traffic_light['redLed'])
def eyes (left, right):
    if(left['red']) == 1:
        lr.on()
    else:
        lr.off()
    if(left['green']) == 1:
        lg.on()
    else:
        lg.off()
    if(left['blue']) == 1:
        lb.on()
    else:
        lb.off()

def main():
    print("Welcome To The STEAM Clown Makey Bot")
    traffic_light = {'redLed' : 1, 'yellowLed' : 1, 'greenLed' : 1}
    lefteye = {'red':1,'green':1,'blue':1}
    righteye = {'red':1,'green':1,'blue':1}
    traffic(traffic_light)
    eyes(lefteye, righteye)
main()
