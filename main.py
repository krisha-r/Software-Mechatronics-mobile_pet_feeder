from machine import Pin, time_pulse_us, PWM
from time import sleep, sleep_us

class Servo:
    def __init__(self, pin, minduty=1638, maxduty=4915):
        self.servo = PWM(Pin(pin))
        self.servo.freq(50)
        self.minduty = minduty
        self.maxduty = maxduty

    def set_angle(self, angle):
        duty = int(self.minduty + (angle / 180) * (self.maxduty - self.minduty))        
        self.servo.duty_u16(duty)

class Steppermotor:
    def __init__(self, pins, delay = 0.005):
        self.pins = [Pin(pin, Pin.OUT) for pin in pins]
        self.delay = delay
        self.step_sequence = [
            [1, 0, 0, 1],  
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
        ]

    def move(self, steps, direction=1):
        seq = len(self.step_sequence)
        for i in range(steps):
            for i in range(seq):
                for pin in range(4):
                    self.pins[pin].value(self.step_sequence[i][pin])
                sleep_us(int(self.delay * 350_000))

class Boolean:
    def __init__(self):
        self.objectDetected = False
  
class Sensor(Boolean):
    def __init__(self, sensorPin):
        super().__init__()
        self.sensorPin = sensorPin
        
    def setUp():
        self.sensorPin = Pin(sensorPin, Pin.OUT)   

    def sendData(self):
        pass

class UltrasonicSensor(Sensor):
    def __init__(self, sensorPin, echoPin):
        super().__init__(sensorPin)
        self.detectDistance = 60
        self.echoPin = echoPin
    
    def setUp():
        super().setUp()
        self.echoPin = Pin(echoPin, Pin.IN)

    def checkData(self):    
        self.sensorPin.off()
        self.sensorPin.sleep_us(2)
        self.sensorPin.on()
        self.sensorPin.sleep_us(10)
        self.sensorPin.off()

        pulse_time = time_pulse_us(self.echoPin, 1, 25000)  

        if pulse_time > 0:
            distance = (pulse_time / 2) / 29.1 
            if distance < self.detectDistance:
                self.objectDetected = True        
        else:
            self.objectDetected = False
        
    def sendData(self):
        checkData()
        return self.objectDetected


class PIRsensor(Sensor):
    def __init__(self, sensorPin):
        super().__init__(sensorPin)
    
    def setUp(self):
        self.sensorPin = Pin(sensorPin, Pin.In)
    
    def checkData(self):
        if self.sensorPin.value():
            self.objectDetected = True
        else:
            self.objectDetected = False
        
        return self.objectDetected
    
    def sendData(self):
        checkData()
        return self.objectDetected


class Button(Boolean):
    def __init__(self, button_pin):
        super.__init__()
        self.button_pin = button_pin
        self.button_pressed = False
    
    def setUp():
        self.button_pin = Pin(button_pin, Pin.IN, Pin.PULL_UP)

    def button_pressed():
        first = button.value()
        time.sleep(0.01)
        second = button.value()
        if first and not second and not self.button_pressed:
            self.button_pressed = True
        else:
            self.button_pressed = False
        return self.button_pressed
    
            


#ultrasonic_sensor = UltrasonicSensor({trig_pin}, {echo_pin})
#pir_sensor = PIRsensor({pin})
button = Button(16)
left_motor = Steppermotor(pins=[18, 19, 20, 21])
right_motor = Steppermotor(pins=[13, 12, 11, 10])

#ultrasonic_sensor.setUp()
#pir_sensor.setUp()
button.setUp()

while True:
    while button.button_pressed():
        while True:#not ultrasonic_sensor.checkData() and not pir_sensor.checkData():
            left_motor.move(25)
            right_motor.move(25)
        #while ultrasonic_sensor.checkData() and not pir_sensor.checkData():
        #    left_motor.move(512) #change step num later
        #while ultrasonic_sensor.checkData() and pir_sensor.checkData():
        #    {servo class}
                
    button.button_pressed()
    
                
                
                
        
        
        
        
        


