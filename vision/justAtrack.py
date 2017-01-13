'''
    File name: justAtrack.py
    Author: Justin Punzalan
    Date created: 1/12/2017
    Date last modified: 1/12/2017
    Python Version: 2.7
'''

import cv2
import numpy as np
#pip install pynetworktables
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Change the address to actual IP
ip = "10.0.4.215"
# Use "Localhost" for local testing
NetworkTables.initialize("localhost")

# sd stands for SmartDashboard
sd = NetworkTables.getTable("Vision/trackTarget")

#Stuff that's sent to robot
targetCenterX = 0

#capture from camera at location 0
cap = cv2.VideoCapture(0)
#set the width and height
cap.set(3,640)
cap.set(4,480)

# Runs forever, might want to toggle instead
while 1:

    # The current frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # TODO: Add Slider on Web/SmartDash
    # define range of blue color in HSV
    lower_color = np.array([110,50,50])
    upper_color = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_color, upper_color)
    im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # Cannot get argmax of an empty sequence
    if len(contours) <= 0:
        targetCenterX = 0
    else:
        # Finds greatest area
        # Biggest area = target
        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)

        # Finds centerX of target
        M = cv2.moments(contours[max_index])
        # Eliminates "ZeroDivisionError: float division by zero"
        if not (M["m00"] <= 0):
            targetCenterX = int(M["m10"] / M["m00"])

    # Displays HSV/HSL View for tuning
    cv2.imshow('mask',mask)

    # Sends centerX to Robot via Network Table
    sd.putNumber('centerX', targetCenterX)
    print "Center Target X: ", targetCenterX

    # Screen Refresh Rate in ms
    key = cv2.waitKey(19)
    
    # Kills process if interupted
    if key == 27:
        break

cv2.destroyAllWindows() 
cv2.VideoCapture(0).release()
