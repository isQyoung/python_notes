import cv2 as cv
import numpy as np
import pyautogui

img = cv.imread('pdf.png', 0)
img2 = img.copy()
pyautogui.screenshot("screen.png")
template = cv.imread('screen.png', 0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    #cv.rectangle(template, top_left, (top_left[0] + w, top_left[1] + h), (0, 0, 255), 2)
    cv.rectangle(img, top_left, bottom_right, 255, 2)
    cv.imwrite(f'{meth}-res.png', template)
