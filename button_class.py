from machine import Pin
import time

class Button():
    def __init__(self, button_pin):
        self.button_pin = button_pin
        self.button_pressed = False
        self.on = False
    
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
    
            
  
        
