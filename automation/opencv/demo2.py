# 最佳匹配
import pyautogui
import cv2
import time

pyautogui.screenshot("screen.png")
img_tmp = cv2.imread('screen.png')
img_src = cv2.imread('grass.png')
method = cv2.TM_SQDIFF_NORMED
result = cv2.matchTemplate(img_src, img_tmp, method)
# 只需要最小平方差mnloc
mn, mx, mnloc, mxloc = cv2.minMaxLoc(result)
mpx, mpy = mnloc  # 获得最小坐标
trows, tcols = img_src.shape[:2]  # 获取图片的宽度
axis = [mpx + tcols / 2, mpy + trows / 2]
# 将小图片用红线在大图片中圈出来
# cv2.rectangle(img_tmp, (mpx, mpy), (mpx + tcols, mpy + trows), (0, 0, 255), 2)
# cv2.imshow('output', img_tmp)
# cv2.waitKey(0)
pyautogui.moveTo(axis[0], axis[1], duration=0.25)  # 移动到目标
pyautogui.click(clicks=1)