import cv2
import numpy as np
from matplotlib import pyplot as plt

img_name = 'P3/P3_016_27.jpg'
img = cv2.imread(img_name,0)
img = img[65:700, 50:950].copy()
img = cv2.medianBlur(img,3)

dst = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
circles = cv2.HoughCircles(dst, cv2.HOUGH_GRADIENT,1,11,
                            param1=5,param2=13,minRadius=7,maxRadius=20)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)

text = "Image: " + img_name
cv2.putText(img, text, (10, 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 1)   
text = "Number of pills: " + str(len(circles[0]))
cv2.putText(img, text, (10, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)    

cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
