import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch
from collections import Counter
from scipy.optimize import linear_sum_assignment
import math
from collections import Counter

count = []
mode = 0
infine = [9999, 9999]

images = []


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
    images.append(dst)

    return points


def get_dist(ord_list):
    # row = len(ord_list[0])
    # col = len(ord_list)
    rows = []
    cols = []

    for i in range(len(ord_list) - 1):
        before = ord_list[i]
        after = ord_list[i + 1]

        # print("==================================")
        # print(before)
        # print("==================================")
        # print(after)
        # print("==================================")

        dst_list = []

        for j in range(len(before)):  # needs to modify
            p = before[j]
            dst = []
            for k in range(len(after)):
                q = after[k]
                dst.append(int(math.dist(p, q)))
            dst_list.append(dst)
        # print(dst_list)
        # print(np.array(dst_list).shape)
        row_ind, col_ind = linear_sum_assignment(dst_list)
        rows.append(row_ind)
        cols.append(col_ind)

    return rows, cols


if __name__ == "__main__":
    img_list = import_pillGroup(64, 3)
    # print(img_list)
    # print("=============================")

    ord_list = []
    len_list = []
    for i in range(10):
        # print(img_list[i])
        ord = detect_pill(img_list[i])
        ord_list.append(ord)
        len_list.append(len(ord))

    print(len_list)
    cnt = Counter(len_list)
    max_pill = cnt.most_common()
    print(max_pill[0][0])
    max_len = max(len_list)
    for ord in ord_list:
        diff = max_len - len(ord)
        if diff != 0:
            for i in range(diff):
                ord.append(infine)
            # print(ord)
            # print(len(ord))

    # print(ord_list)
    # print(np.array(ord_list).shape)
    # print("=============================")

    rows, cols = get_dist(ord_list)
    # print("=============================")
    # print(rows)
    # print("=============================")
    # print(cols)

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(1, 5, 1)
    plt.imshow(images[0], "gray")

    for i in range(len(ord_list) - 1):
        if i < 4:
            ax2 = fig.add_subplot(1, 5, i + 2)
            plt.imshow(images[i + 1], "gray")
        else:
            ax2 = fig.add_subplot(2, 5, 10 - (i - 4))
            plt.imshow(images[i + 1], "gray")

        for j in range(len(cols[i])):
            xyA = (ord_list[i][j][0], ord_list[i][j][1])
            xyB = (ord_list[i + 1][cols[i][j]][0], ord_list[i + 1][cols[i][j]][1])
            if xyA == (9999, 9999) or xyB == (9999, 9999):
                pass
            con = ConnectionPatch(
                xyA=xyA,
                xyB=xyB,
                coordsA="data",
                coordsB="data",
                axesA=ax2,
                axesB=ax1,
                color=((i * 15) / 255, 0, 0),
            )
            ax2.add_artist(con)
        ax1 = ax2
    # plt.show()
    plt.text(0.5, 0.5, "num(Pills): " + str(max_pill[0][0]))
    plt.savefig("pills.png", dpi=500)
