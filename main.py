from tkinter import * 
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
import time

led = LED(5) #initializing LED

def dot(): #define the dot function
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    
    
def dash(): #define the dash function
    led.on()
    time.sleep(1.5)
    led.off()
    time.sleep(0.5)
    
dict = { 'A':'.-', 'B':'-...', #dictionary to store values of morse alphabetically
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'
                }


        
  
win = Tk() #opening the GUI window
win.title("Text To Morse") #GUI title
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold") #setting of font
                                  

def close(): #creating function
    win.destroy()
    GPIO.cleanup() #GUI exit

def convertAndBlink(): #creating function
    text1 = textInput.get().upper() #text is in uppercase
    text = list(text1) #using list to create string into char
    print(text)

    
    for x in text: #for loop
        morse = list(dict[x]) #set morse code as list
        for y in morse: 
            if(y == "."): #creating a condition to implement and print dot
                dot()
            elif(y == "-"): #else if condition to print dash
                dash()


textInput = Entry(win) #take the user input
textInput.pack() #declares the position


    ## Buttons - Instead of using grid spacing, we can '.pack()' to order our widgets respectively.
sendButton = Button(win, text = 'Submit', command = convertAndBlink) #setting the submit button and giving command to convert the string value to morse code and blink accordingly
sendButton.pack(side= 'top') #assigning the top position
closeButton = Button(win, text = 'Exit', command = close) #button for exit
closeButton.pack(side = 'bottom') #assigning the bottom position to close button

win.mainloop() #runs the tkinter loop
