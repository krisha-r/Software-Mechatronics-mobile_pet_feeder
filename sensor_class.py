from machine import Pin, time_pulse_us

#Parent sensor Class
class Sensor:
    def __init__(self, sensorPin):
        self.sensorPin = sensorPin
        self.objectDetected = False
    #Set up sensor
    def setUp():
        self.sensorPin = Pin(sensorPin, Pin.OUT)   

    def sendData(self):
        pass


#Chidl class of Sensor Class
class UltrasonicSensor(Sensor):
    def __init__(self, sensorPin, echoPin):
        super().__init__(sensorPin)
        self.detectDistance = 60
        self.echoPin = echoPin
    #Set up the ultrasonic sensor
    def setUp():
        super().setUp()
        self.echoPin = Pin(echoPin, Pin.IN)
    #Checks if there is an object detected and return True or False
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
    #Sends data to main.py
    def sendData(self):
        checkData()
        return self.objectDetected

#Child class of Sensor Class
class PIRsensor(Sensor):
    def __init__(self, sensorPin):
        super().__init__(sensorPin)
    
    #Set up PIR Sensor
    def setUp(self):
        self.sensorPin = Pin(sensorPin, Pin.In)
    #Check is motion detected, and return True or False
    def checkData(self):
        if self.sensorPin.value():
            self.objectDetected = True
        else:
            self.objectDetected = False
        
        return self.objectDetected
    
    #Send data to main.py
    def sendData(self):
        checkData()
        return self.objectDetected

