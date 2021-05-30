import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('P3_064_27.jpg',0)
img = cv2.medianBlur(img,3)

dst = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

circles = cv2.HoughCircles(dst, cv2.HOUGH_GRADIENT,1,11,
                            param1=5,param2=13,minRadius=7,maxRadius=20)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
