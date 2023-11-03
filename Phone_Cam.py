# -*- coding: utf-8 -*-
"""

@author: DS-Alex-ML

"""

import cv2 as cv

# Browser IP Cam Access of the app DroidCam, example: http://192.168.1.92:4747
#cam = cv.VideoCapture("http://192.168.1.92:4747")

# To start with the computer cam
cam = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, real_time = cam.read()

    # Our operations on the video real time come here
    gray = cv.cvtColor(real_time, cv.COLOR_BGR2GRAY)

    # Display the resulting real time video
    cv.imshow('Phone Cam',gray)
    
    # To end the video in real time, press ESC
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the cam
cam.release()
cv.destroyAllWindows()