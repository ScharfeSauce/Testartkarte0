import sqlite3
from gpiozero import LED
from gpiozero import Button
import time
import datetime


class Testat():
    def __init__(self, led):
        self.led = led
        self.time = ""

    def klick_on(self):
        self.led.on()
        self.time = datetime.datetime.now()

    def klick_off(self):
        self.led.off()
        self.time = datetime.datetime.now()

    def event(self):
        if not self.led.is_lit:
            self.klick_on()

        elif self.led.is_lit:
            self.klick_off()
        conn = sqlite3.connect("/home/pi/Desktop/Physical Computing/Testatkarte0/LED.db")
        c = conn.cursor()
        c.execute(f"INSERT INTO tblLED VALUES (null, '{self.led.is_lit}', '{self.time}')")
        print(f"{self.led.is_lit}, {self.time}")
        conn.commit()

taster1 = Button(23, pull_up= False)
red = LED(17)


try:
    test = Testat(red)
    taster1.when_released = test.event
except KeyboardInterrupt:
    red.close()