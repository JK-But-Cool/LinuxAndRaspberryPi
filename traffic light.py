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
    rfd = [traffic_light, lefteye, righteye]
    return(rfd)
    
def eyes (rfd):
    lr.value = (rfd[1]['red'])
    lg.value = (rfd[1]['green'])
    lb.value = (rfd[1]['blue'])
    rr.value = (rfd[2]['red'])
    rg.value = (rfd[2]['green'])
    rb.value = (rfd[2]['blue'])

def main():
    data = (get_robot_feature_data())
    traffic(data)
    eyes(data)
main()
