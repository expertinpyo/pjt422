import os
from gpiozero import Servo
import RPi.GPIO as GPIO
import RPi_I2C_driver
from mfrc522 import SimpleMFRC522
from gpiozero import LED
from time import *

servo1 = Servo(16) # Continuous Rotation Servo
servo2 = 26 # 180 degree Rotation servo
triggerPin = 14 # trig for ultrasonic
echoPin = 4 # echo for ultrasonic
redLED = LED(23)
greenLED = LED(24)
btnPin = 18

max_capacity = 30.58
min_capacity = 12.92

information = {
#     "deviceID",
#     "userID",
#     "type",
#     "capacityRate",
    "userGroup" : "none",
#     "startTime",
    "frontDoorState":"close",
}

def open_slide_door():
    servo1.value = 0.1
    sleep(1.5)
    servo1.detach()


def close_slide_door():
    servo1.value = -0.5
    sleep(1.55)
    servo1.detach()


def set_gpio_for_front_door():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo2, GPIO.OUT)
    pwm = GPIO.PWM(servo2, 50)
    pwm.start(0)
    return pwm
    
    
def unlock_front_door(pwm):
    GPIO.setup(servo2, GPIO.OUT)
    pwm.ChangeDutyCycle(3) #unlock
    sleep(0.3)
    GPIO.setup(servo2, GPIO.IN)
    sleep(1.7)
    
    
def lock_front_door(pwm):
    GPIO.setup(servo2, GPIO.OUT)
    pwm.ChangeDutyCycle(8) #lock
    sleep(0.3)
    GPIO.setup(servo2, GPIO.IN)
    sleep(1.7)

    
def cleanup_for_front_door(pwm):
    pwm.stop()
    GPIO.cleanup()
    
    
def set_gpio_for_capacity_check():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(triggerPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)
    
    
def capacity_check():
    GPIO.output(triggerPin, GPIO.LOW)
    sleep(0.00001)
    GPIO.output(triggerPin, GPIO.HIGH)

    while GPIO.input(echoPin) == 0:
        start = time()
    while GPIO.input(echoPin) == 1:
        stop = time()

    rtTotime = stop - start

    distance = round(rtTotime * ( 34000 / 2 ),2)
    return distance


def cleanup_for_capacity_check():
    GPIO.cleanup()
    
    
def current_capacity_rate():
    currentDistance = capacity_check()
    rate = round((max_capacity - currentDistance)/(max_capacity - min_capacity),2)*100
    if rate<0 : return 0
    else : return rate


def set_display_lcd():
    lcd = RPi_I2C_driver.lcd(0x27)
    lcd.clear()
    return lcd


def display_lcd(lcd, content):
    lcd.print(content)
    sleep(5)
    
    
def clear_lcd(lcd):
    lcd.clear()


def getuserID():
    print("tag")
    id = SimpleMFRC522().read()[0]
    return id


def get_deviceID():
    serialID = os.popen("cat /proc/cpuinfo | grep Serial | awk '{print $3}'").read()
    return serialID


def led_on(colorLED):
    colorLED.on()


def led_off(colorLED):
    colorLED.off()
    

def pass_auth():
    led_on(greenLED)
    open_slide_door()
  
  
def fail_auth():
    led_on(redLED)
    sleep(3)
    led_off(redLED)


def the_last_action():
    close_slide_door()
    sleep(1.5)
    led_off(greenLED)

