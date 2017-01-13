##
## Robot Test 3
## Directional Control
##

import zbIrButtonMap as Buttons
import ZeroBorg
import time

from mpu6050 import MPU6050
import smbus


address = 0x68
bus = smbus.SMBus(1)
##bus = 1

sensor = MPU6050(bus,address,"MPU6050")
sensor.read_raw_data()

from pid import PID

ZB = ZeroBorg.ZeroBorg()
ZB.Init()

ZB.SetCommsFailsafe(False)
ZB.ResetEpo()

pid =PID(0.075,0.0,0.0)

maxPower = 0.75

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def Move(left, right):
    #print '%0.2f | %0.2f' % (left, right)
    ZB.SetMotor1(-left * maxPower)
    ZB.SetMotor3(right * maxPower)
    

def MoveForward():
    Move(+1.0, +1.0)

def MoveBackward():
    Move(-1.0, -1.0)

def SpinLeft():
    Move(-1.0, +1.0)

def SpinRight():
    Move(+1.0, -1.0)

def Stop():
    Move(0.0, 0.0)
    
def Shutdown():
    global running
    running = False

global running
running = True
ZB.SetLedIr(True)


set_point = 0.0

try:
    while running:
        sensor.read_raw_data()
        pitch, roll = sensor.read_pitch_roll_degrees()
        pid.setPoint(set_point)
        output = pid.update(-roll)
        output = clamp(output,-1,1)
        
        if abs(roll) > 45:
            ZB.SetLed(True)
            running = False
        else:
            ZB.SetLed(False)
            
        motor = output
        
        ZB.SetMotor1(motor)
        ZB.SetMotor3(motor)
        time.sleep(0.1)
        print("Roll: {}, output: {}".format(roll,output))
        
    
    ZB.MotorsOff()
    ZB.SetLed(False)
            
    
except KeyboardInterrupt:
    ZB.MotorsOff()
    ZB.SetLed(False)
except Exception as e:
    print(e)
    
    


