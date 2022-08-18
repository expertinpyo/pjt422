import os
import RPi.GPIO as GPIO
from gpiozero import Servo, LED, Button
from . import RPi_I2C_driver
from mfrc522 import SimpleMFRC522
from time import time
from asyncio import sleep

servo1 = Servo(16) # Continuous Rotation Servo
servo2 = 26 # 180 degree Rotation servo
triggerPin = 14 # trig for ultrasonic
echoPin = 4 # echo for ultrasonic
redLED = LED(23)
greenLED = LED(24)
rfid = SimpleMFRC522()
btn = Button(18)

MAX_CAPACITY = 30.58
MIN_CAPACITY = 12.92

async def open_slide_door():
    servo1.value = 0.3
    await sleep(1.2)
    servo1.detach()


async def close_slide_door():
    servo1.value = -0.7
    await sleep(1.2)
    servo1.detach()


def set_gpio_for_front_door():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo2, GPIO.OUT)
    pwm = GPIO.PWM(servo2, 50)
    pwm.start(0)
    return pwm


async def unlock_front_door(pwm):
    GPIO.setup(servo2, GPIO.OUT)
    pwm.ChangeDutyCycle(3) #unlock
    await sleep(0.3)
    GPIO.setup(servo2, GPIO.IN)
    await sleep(1.7)


async def lock_front_door(pwm):
    GPIO.setup(servo2, GPIO.OUT)
    pwm.ChangeDutyCycle(8) #lock
    await sleep(0.3)
    GPIO.setup(servo2, GPIO.IN)
    await sleep(1.7)


def cleanup_for_front_door(pwm):
    pwm.stop()
    GPIO.cleanup()


def set_gpio_for_capacity_check():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(triggerPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)


async def capacity_check():
    GPIO.output(triggerPin, GPIO.LOW)
    await sleep(0.00001)
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


async def current_capacity_rate():
    currentDistance = await capacity_check()
    rate = round((currentDistance - MIN_CAPACITY)/(MAX_CAPACITY - MIN_CAPACITY),2)
    if rate < 0:
        return 0
    if rate > 1:
        return 1
    return rate


def set_display_lcd():
    lcd = RPi_I2C_driver.lcd(0x27)
    lcd.clear()
    return lcd


async def display_lcd(lcd, content):
    lcd.print(content)
    await sleep(5)


def clear_lcd(lcd):
    lcd.clear()


def getuserID():
    print("tag")
    id = rfid.read_id_no_block()
    return id


def get_deviceID():
    serialID = os.popen("cat /proc/cpuinfo | grep Serial | awk '{print $3}'").read()
    return serialID


def led_on(colorLED):
    colorLED.on()


def led_off(colorLED):
    colorLED.off()

def is_btn_pressed():
    return btn.is_pressed

async def pass_auth():
    led_on(greenLED)
    await open_slide_door()


async def fail_auth():
    led_on(redLED)
    await sleep(3)
    led_off(redLED)


async def the_last_action():
    led_off(greenLED)
    await close_slide_door()
