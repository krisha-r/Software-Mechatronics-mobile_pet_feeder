from machine import Pin, time_pulse_us

class Sensor:
    def __init__(self, sensorPin):
        self.sensorPin = sensorPin
        self.objectDetected = False
        
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
