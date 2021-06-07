import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
from scipy.optimize import linear_sum_assignment
import math

count = []
mode = 0
infine = [9999, 9999]


def import_pillGroup(pillnum, groupnum):
    img_list = []

    prefix = "S3_" + str(pillnum).zfill(3) + "_" + str(groupnum).zfill(2)

    for f in os.listdir("S3"):
        if f.startswith(prefix):
            img_list.append(f)

    return img_list


def detect_pill(img):
    img = "S3/" + img
    img = cv2.imread(img, 0)
    img = img[115:760, 50:980].copy()
    img = cv2.medianBlur(img, 3)

    dst = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # dst = cv2.medianBlur(dst, 3)

    circles = cv2.HoughCircles(
        dst, cv2.HOUGH_GRADIENT, 1, 11, param1=5, param2=13, minRadius=7, maxRadius=20
    )
    circles = np.uint16(np.around(circles))

    points = []
    for i in circles[0, :]:
        points.append([i[0], i[1]])

    count.append(len(points))

    return points


def get_dist(ord_list):
    # row = len(ord_list[0])
    # col = len(ord_list)
    rows = []
    cols = []

    for i in range(len(ord_list) - 1):
        before = ord_list[i]
        after = ord_list[i + 1]

        print("==================================")
        print(before)
        print("==================================")
        print(after)
        print("==================================")

        dst_list = []

        for j in range(len(before)):  # needs to modify
            p = before[j]
            dst = []
            for k in range(len(after)):
                q = after[k]
                dst.append(int(math.dist(p, q)))
            dst_list.append(dst)
        print(dst_list)
        print(np.array(dst_list).shape)
        row_ind, col_ind = linear_sum_assignment(dst_list)
        rows.append(row_ind)
        cols.append(col_ind)

    return rows, cols


if __name__ == "__main__":
    img_list = import_pillGroup(64, 1)
    # print(img_list)
    # print("=============================")

    ord_list = []
    len_list = []
    for i in range(10):
        # print(img_list[i])
        ord = detect_pill(img_list[i])
        ord_list.append(ord)
        len_list.append(len(ord))

    max_len = max(len_list)
    for ord in ord_list:
        diff = max_len - len(ord)
        if diff != 0:
            for i in range(diff):
                ord.append(infine)
            # print(ord)
            # print(len(ord))

    # print(np.array(ord_list).shape)
    # print("=============================")

    rows, cols = get_dist(ord_list)
    print("=============================")
    print(rows)
    print("=============================")
    print(cols)
