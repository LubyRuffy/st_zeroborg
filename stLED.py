import ZeroBorg
import zbIrButtonMap as Buttons
import time

zb = ZeroBorg.ZeroBorg()
zb.Init()
zb.ResetEpo()

#Get Message to clear the queue
zb.GetIrMessage()

try:
    running = True
    while running:
        if zb.HasNewIrMessage():
            pressedButtonCode = zb.GetIrMessage()
            if pressedButtonCode == Buttons.IR_up:
                zb.SetLed(1)
            elif pressedButtonCode == Buttons.IR_down:
                zb.SetLed(0)
            elif pressedButtonCode == Buttons.IR_left:
                print("Exit")
                running = False
            else:
                print("Not recognised")
            time.sleep(0.1)


except KeyboardInterrupt:
    # CTRL+C exit, disable all drives
    zb.MotorsOff()
