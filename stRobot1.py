##
## Robot Test 1
## Basic Motor Control using IR Remote
##

import zbIrButtonMap as Buttons
import ZeroBorg
import time

ZB = ZeroBorg.ZeroBorg()
ZB.Init()

ZB.SetCommsFailsafe(False)
ZB.ResetEpo()

maxPower = 0.75

def Move(left, right):
    #print '%0.2f | %0.2f' % (left, right)
    ZB.SetMotor1(-left * maxPower)
    ZB.SetMotor2(-left * maxPower)
    ZB.SetMotor3(right * maxPower)
    ZB.SetMotor4(right * maxPower)
    

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
    
buttonCommands = {                      # A list of all the allowed buttons and their corresponding movement settings
    Buttons.SAMSUNG_TV.IR_power:        Shutdown,
    Buttons.SAMSUNG_TV.IR_2:            MoveForward,
    Buttons.SAMSUNG_TV.IR_4:            SpinLeft,
    Buttons.SAMSUNG_TV.IR_5:            Stop,
    Buttons.SAMSUNG_TV.IR_6:            SpinRight,
    Buttons.SAMSUNG_TV.IR_8:            MoveBackward,
    Buttons.SAMSUNG_TV.IR_up:           MoveForward,
    Buttons.SAMSUNG_TV.IR_left:         SpinLeft,
    Buttons.SAMSUNG_TV.IR_right:        SpinRight,
    Buttons.SAMSUNG_TV.IR_down:         MoveBackward,
    Buttons.SAMSUNG_TV.IR_select:       Stop,
    Buttons.SAMSUNG_TV.IR_pause:        Stop,
    Buttons.SAMSUNG_TV.IR_stop:         Stop,
}

global running
running = True
ZB.SetLedIr(True)
ZB.SetLed(True)

try:
    while running:
        if ZB.HasNewIrMessage():
            pressedButton = ZB.GetIrMessage()
            if buttonCommands.has_key(pressedButton):
                buttonCommands[pressedButton]()
            else:
                pass
        time.sleep(0.1)
    ZB.MotorsOff()
    ZB.SetLed(False)
            
    
except KeyboardInterrupt:
    ZB.MotorsOff()
    ZB.SetLed(False)
    


