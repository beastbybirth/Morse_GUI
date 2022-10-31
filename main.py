from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
import time

led = LED(5)

def dot():
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    
    
def dash():
    led.on()
    time.sleep(1.5)
    led.off()
    time.sleep(0.5)
    
dict = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'
                }


        
  
win = Tk()
win.title("Text To Morse")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
                                  

def close():
    win.destroy()
    GPIO.cleanup()

def convertAndBlink():
    text1 = textInput.get().upper()
    text = list(text1)
    print(text)

    
    for x in text:
        morse = list(dict[x])
        for y in morse:
            if(y == "."):
                dot()
            elif(y == "-"):
                dash()


textInput = Entry(win)
textInput.pack()


    ## Buttons - Instead of using grid spacing, we can '.pack()' to order our widgets respectively.
sendButton = Button(win, text = 'Submit', command = convertAndBlink)
sendButton.pack(side= 'top')
closeButton = Button(win, text = 'Exit', command = close)
closeButton.pack(side = 'bottom')

win.mainloop()
