import cv2 as cv
import numpy as np
import pyautogui
from matplotlib import pyplot as plt


pyautogui.screenshot("screen.png")
img_rgb = cv.imread('screen.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('excel.png', 0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    print("移动到 " + str(pt))
    #pyautogui.moveTo(pt[0], pt[1], duration=0.5)
    #pyautogui.click()
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
cv.imwrite('res.png', img_rgb)
plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_rgb, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()
