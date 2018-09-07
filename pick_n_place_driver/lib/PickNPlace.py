import lib.StepperDriver as StepperDriver


class PickNPlace:
    X_STEPPER = 1
    Z_STEPPER = 2

    def __init__(self):
        self.mh = StepperDriver.Adafruit_MotorHAT(freq=1600)
        self.x_stepper = self.mh.getStepper(200, PickNPlace.X_STEPPER)
        self.z_stepper = self.mh.getStepper(200, PickNPlace.Z_STEPPER)
        self.x_stepper.setSpeed(10) # Note speed dosen't work
        self.z_stepper.setSpeed(10)
   
    def down(self, steps):
        self.z_stepper.step(steps, StepperDriver.Adafruit_MotorHAT.BACKWARD,  StepperDriver.Adafruit_MotorHAT.DOUBLE)

    def up(self, steps):
        self.z_stepper.step(steps, StepperDriver.Adafruit_MotorHAT.FORWARD,  StepperDriver.Adafruit_MotorHAT.DOUBLE) 
    
    def left(self, steps):
        self.x_stepper.step(steps, StepperDriver.Adafruit_MotorHAT.BACKWARD,  StepperDriver.Adafruit_MotorHAT.DOUBLE)

    def right(self, steps):
        self.x_stepper.step(steps, StepperDriver.Adafruit_MotorHAT.FORWARD,  StepperDriver.Adafruit_MotorHAT.DOUBLE)
