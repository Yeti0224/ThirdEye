import cv2
from rpi_ws281x import *
import time

# Camera Intialization
capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_car.xml')

# LED Initialization
led = Adafruit_NeoPixel(15, 18, 800000, 10, False, 180, 0) # # of leds, GPIO pin #, Frequency, DMA, Invert, Brightness, Channel
led.begin()
color = Color(0, 0, 0)

while True:
    isTrue, frame = capture.read()
    if isTrue == False: # Checks if webcam is working
        break
    
    # Change frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect cars
    cars = cascade.detectMultiScale(gray, 1.4, 2)
    
    if len(cars) == 0:
        color = Color(0, 0, 0) # No cars? Turn off
    else:
        color = Color(255, 0, 0) # Have cars? Turn on
    
    # Code to check camera and detection
    #for (x, y, width, height) in cars:
        #cv2.rectangle(frame, (x, y),(x + width, y + height), (0, 0, 255), 2)
    #cv2.imshow("Car Detection", frame)
    
    # Turn on/off the LEDs
    for i in range(15):
        led.setPixelColor(i, color)
        led.show()
        time.sleep(50/1000.0)
    
    # Press ESC to break/stop camera
    if cv2.waitKey(33) == 27:
        break


# Turns off LED and Camera
for i in range(15):
    led.setPixelColor(i, Color(0, 0, 0))
    led.show()
capture.release()
cv2.destroyAllWindows()