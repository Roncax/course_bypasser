import pyautogui
import time
import numpy as np
from PIL import Image


def image_compare(image_1, image_2):
    arr1 = np.array(image_1)
    arr2 = np.array(image_2)
    if arr1.shape != arr2.shape:
        return False
    maxdiff = np.max(np.abs(arr1 - arr2))
    return maxdiff == 0

def image_compare_file(filename_1, filename_2):
    im1 = Image.open(filename_1)
    im2 = Image.open(filename_2)
    return image_compare(im1, im2)


screenshot_region = (537,499,136,22)
myScreenshot_current = pyautogui.screenshot(region=screenshot_region)
myScreenshot_current.save(r'current.png')

while(True):
    myScreenshot_next = pyautogui.screenshot(region=screenshot_region)
    myScreenshot_next.save(r'next.png')
    time.sleep(2)
    if image_compare_file('current.png','next.png'):
        pyautogui.click(x=610, y=540)
        time.sleep(6)
    else:
        pass
    myScreenshot_next.save(r'current.png')

# while(True):
#     pos = pyautogui.position()
#     print(pos)
#     time.sleep(1) # Sleep for 3 seconds