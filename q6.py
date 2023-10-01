import cv2
import numpy as np


original_image = cv2.imread('finger-bones.jpg')
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])
mask_yellow = cv2.inRange(hsv_image, yellow_lower, yellow_upper)

blue_lower = np.array([110, 50, 50])
blue_upper = np.array([130, 255, 255])
mask_blue = cv2.inRange(hsv_image, blue_lower, blue_upper)

green_lower = np.array([50, 100, 100])
green_upper = np.array([70, 255, 255])
mask_green = cv2.inRange(hsv_image, green_lower, green_upper)

brown_lower = np.array([10, 100, 100])
brown_upper = np.array([20, 255, 255])
mask_brown = cv2.inRange(hsv_image, brown_lower, brown_upper)

light_blue_lower = np.array([90, 100, 100])
light_blue_upper = np.array([110, 255, 255])
mask_light_blue = cv2.inRange(hsv_image, light_blue_lower, light_blue_upper)


contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_brown, _ = cv2.findContours(mask_brown, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_light_blue, _ = cv2.findContours(mask_light_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


max_width_yellow = 0
max_height_yellow = 0
max_width_blue = 0
max_height_blue = 0
max_width_green = 0
max_height_green = 0
max_width_brown = 0
max_height_brown = 0
max_width_light_blue = 0
max_height_light_blue = 0
o_image = original_image.copy()


for c in contours_yellow:
    x, y, width, height = cv2.boundingRect(c)
    
    if width > max_width_yellow:
        max_width_yellow = width
    if height > max_height_yellow:
        max_height_yellow = height
    cv2.drawContours(o_image, [c], 0, (0, 255, 0), 2)


for c in contours_blue:
    x, y, width, height = cv2.boundingRect(c)
    
    if width > max_width_blue:
        max_width_blue = width
    if height > max_height_blue:
        max_height_blue = height
    cv2.drawContours(o_image, [c], 0, (0, 255, 0), 2)


for c in contours_green:
    x, y, width, height = cv2.boundingRect(c)
    
    if width > max_width_green:
        max_width_green = width
    if height > max_height_green:
        max_height_green = height
    cv2.drawContours(o_image, [c], 0, (0, 255, 0), 2)


for c in contours_brown:
    x, y, width, height = cv2.boundingRect(c)
    
    if width > max_width_brown:
        max_width_brown = width
    if height > max_height_brown:
        max_height_brown = height
    cv2.drawContours(o_image, [c], 0, (0, 255, 0), 2)


for c in contours_light_blue:
    x, y, width, height = cv2.boundingRect(c)
    
    if width > max_width_light_blue:
        max_width_light_blue = width
    if height > max_height_light_blue:
        max_height_light_blue = height
    cv2.drawContours(o_image, [c], 0, (0, 255, 0), 2)



cv2.imshow('Annotated Image', o_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



