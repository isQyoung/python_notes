# 单多图匹配
import cv2 as cv
import numpy as np
import pyautogui

pyautogui.screenshot("screen.png")  # 截全屏大图
img_rgb = cv.imread('screen.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('excel.png', 0)  # 用作匹配的小图
w, h = template.shape[::-1]  # 小图的宽和高
res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)  # 大小图匹配结果
threshold = 0.9  # 匹配度百分比
loc = np.where(res >= threshold)  # 只取匹配度大于threshold的结果
for pt in zip(*loc[::-1]):
    print("移动到 " + str(pt))  # 打印对应的坐标
    pyautogui.moveTo(pt[0], pt[1], duration=0.5)  # 鼠标移动到对应的坐标
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)  # 用红色框出来
cv.imwrite('res.png', img_rgb)  # 生成处理过的图片
