from gpiozero import LED
from gpiozero import PWMLED
import time
redLed = LED(2)
yellowLed = LED(3)
greenLed = LED(18)
lr = PWMLED(17)
lg = PWMLED(27)
lb = PWMLED(22)
rr = PWMLED(13)
rg = PWMLED(19)
rb = PWMLED(26)

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

def rgb (eyedictionary):
    pass
    
def eyes (left, right):
    lr.value = (left['red'])
    lg.value = (left['green'])
    lb.value = (left['blue'])
    rr.value = (right['red'])
    rg.value = (right['green'])
    rb.value = (right['blue'])

def main():
    print("Welcome To The STEAM Clown Makey Bot")
    traffic_light = {'redLed' : 0, 'yellowLed' : 0, 'greenLed' : 0}
    lefteye = {'red':0,'green':0,'blue':0}
    righteye = {'red':0,'green':0,'blue':0}
    trafficflag = False
    while trafficflag == False:
        try:
            x = int(input("input number 0-7: "))
        except:
            print ("NAN")
        else:
            if x <= 7 and x >=0:
                trafficflag = True
                x = bin(x)[2:]
                xcool = []
                for i in x:
                    xcool.append(i)
                while len(xcool) < 3:
                    xcool.insert(0, "0")
                c = 0
                for i in traffic_light:
                    traffic_light[i] = int(xcool[c])
                    print(i)
                    c += 1
            else:
                print("not between 0-7")
    for i in lefteye:
        lefteyeflag = False
        print("changing the left eye",i,"value")
        while lefteyeflag == False:
            try:
                color = float(input("enter a decimal between 0 and 1, including both: "))
            except:
                print("NAN")
            else:
                if(color >= 0 and color <= 1):
                    lefteye[i] = color
                    lefteyeflag = True
                else:
                    print("not in range")
    for i in righteye:
        righteyeflag = False
        print("changing the right eye",i,"value")
        while righteyeflag == False:
            try:
                color = float(input("enter a decimal between 0 and 1, including both: "))
            except:
                print("NAN")
            else:
                if(color >= 0 and color <= 1):
                    righteye[i] = color
                    righteyeflag = True
                else:
                    print("not in range")

    traffic(traffic_light)
    eyes(lefteye, righteye)
main()
