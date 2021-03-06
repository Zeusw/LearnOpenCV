#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-10 20:22:11
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

from matplotlib import pyplot as plt
import numpy as np
import cv2


cap = cv2.VideoCapture(0)
cap.set(3, 1024)
cap.set(4, 768)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 3, 255, -1)

    cv2.imshow('SIFTVideo', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()