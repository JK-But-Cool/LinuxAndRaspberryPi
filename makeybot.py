from gpiozero import LED
from gpiozero import PWMLED
import time
from gpiozero import Servo
from gpiozero import AngularServo
from time import sleep
from threading import Timer
#var = Timer(seconds, code to run)
redLed = LED(2)
yellowLed = LED(3)
greenLed = LED(18)
lr = PWMLED(17)
lg = PWMLED(27)
lb = PWMLED(22)
rr = PWMLED(13)
rg = PWMLED(19)
rb = PWMLED(26)
maxCorrection=0.35
minCorrection=0.35
maxPW=(2.0+maxCorrection)/1000
minPW=(1.0 -minCorrection)/1000
 
servo = AngularServo(16,min_pulse_width=minPW,max_pulse_width=maxPW)
def traffic(rfd):
    if(rfd[0]['redLed']) == 1:
        redLed.on()
    else:
        redLed.off()
    if(rfd[0]['yellowLed']) == 1:
        yellowLed.on()
    else:
        yellowLed.off()
    if(rfd[0]['greenLed']) == 1:
        greenLed.on()
    else:
        greenLed.off()

def get_robot_feature_data():
    lefteye = {'red':0,'green':0,'blue':0}
    righteye = {'red':0,'green':0,'blue':0}
    traffic_light = {'redLed' : 0, 'yellowLed' : 0, 'greenLed' : 0}
    # servo
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
                    c += 1
            else:
                print("not between 0-7")
                
    lefteyeflag = False
    print("changing the rgb value of the left eye")
    while lefteyeflag == False:
        color = input("give a hex code: #").upper()
        if(len(color) != 6): print("not a valid hex code")
        else:
            try: ishex = int(color,16)
            except: print ("not a valid hex code")
            else:
                lefteyeflag = True
                lefteye['red'] = int(color[0:2],16) / 255 * 0.75
                lefteye['green'] = int(color[2:4],16) / 255
                lefteye['blue'] = int(color[4:],16) / 255
    print("changing the rgb value of the right eye")
    
    righteyeflag = False
    while righteyeflag == False:
        color = input("give a hex code: #").upper()
        if(len(color) != 6): print("not a valid hex code")
        else:
            try: ishex = int(color,16)
            except: print ("not a valid hex code")
            else:
                righteyeflag = True
                righteye['red'] = int(color[0:2],16) / 255 * 0.75
                righteye['green'] = int(color[2:4],16) / 255
                righteye['blue'] = int(color[4:],16) / 255
    rfd = [traffic_light, lefteye, righteye]
    return(rfd)
    
def eyes (rfd):
    lr.value = (rfd[1]['red'])
    lg.value = (rfd[1]['green'])
    lb.value = (rfd[1]['blue'])
    rr.value = (rfd[2]['red'])
    rg.value = (rfd[2]['green'])
    rb.value = (rfd[2]['blue'])
def wave():
    while True:
        wave_delay = 0.5
        servo.angle = 90
        sleep(wave_delay)
        servo.angle = -90
        sleep(wave_delay)
def main():
    data = (get_robot_feature_data())
    traffic(data)
    eyes(data)
    wave()
main()

