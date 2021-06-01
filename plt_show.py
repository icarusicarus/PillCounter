import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch
from collections import Counter
from scipy.optimize import linear_sum_assignment
import math


img1 = 'S3_016_02_05.jpg'
img2 = 'S3_016_02_06.jpg'

images = []

count = []
mode = 0

def detect_pill(img):
    img = cv2.imread(img,0)
    img = img[115:760, 50:980].copy()
    img = cv2.medianBlur(img,5)

    dst = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,31,2)

    dst = cv2.medianBlur(dst,3)

    circles = cv2.HoughCircles(dst, cv2.HOUGH_GRADIENT,1,11,
                            param1=5,param2=13,minRadius=7,maxRadius=20)
    circles = np.uint16(np.around(circles))

    points = []
    for i in circles[0,:]:
        points.append([i[0],i[1]])
        
    count.append(len(points))

    images.append(dst)
    return points

def get_dist(points1, points2):
    distance = []

    for i in range(len(points1)):
        x1 = points1[i][0]
        y1 = points1[i][1]
        p1 = points1[i]

        dst = []
        for j in range(len(points2)):
            x2 = points2[j][0]
            y2 = points2[j][1]
            p2 = points2[j]

            # print(x1, y1, x2, y2)
            
            dst.append(int(math.dist(p1, p2)))
        distance.append(dst)
            #distance[i].append(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

    return distance

    

if __name__ == '__main__':
    # import_pill_group(64, 1)
    p1 = detect_pill(img1)
    p2 = detect_pill(img2)
    print(p1)
    print(p2)
    print("=============================")
    dst = get_dist(p1, p2)
    print(dst)
    row_ind, col_ind = linear_sum_assignment(dst)
    print("=============================")

    #plt.subplot(1,2,j+1), plt.imshow(images[j], 'gray')
    fig = plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(121)
    plt.imshow(images[0], 'gray')
    ax2 = fig.add_subplot(122)
    plt.imshow(images[1], 'gray')
    
    for i in range(16):
        xyA = (p1[i][0], p1[i][1])
        xyB = (p2[col_ind[i]][0], p2[col_ind[i]][1])
        con = ConnectionPatch(xyA=xyA, xyB=xyB, coordsA="data", coordsB="data",
                    axesA=ax2, axesB=ax1, color=((i*15)/255,0,0))
        ax2.add_artist(con)
    plt.show()
