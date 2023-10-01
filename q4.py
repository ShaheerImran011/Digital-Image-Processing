
import cv2
import numpy as np

def calculate_area(path_of_image):
    original_image = cv2.imread(path_of_image)
    image_yellow = original_image.copy()
    image_light_gray = original_image.copy()
    image_gray = original_image.copy()
    image_dark_gray = original_image.copy()
    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])
    mask_yellow = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    detected_yellow = cv2.bitwise_and(image_yellow, image_yellow, mask=mask_yellow)
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area_yellow = 0
    for c in contours_yellow:
        area_yellow += cv2.contourArea(c)
        M_yellow = cv2.moments(c)
        if M_yellow["m00"] != 0:
            cx_yellow = int(M_yellow["m10"] / M_yellow["m00"])
            cy_yellow = int(M_yellow["m01"] / M_yellow["m00"])
            cv2.putText(original_image, f"{area_yellow:.2f}", (cx_yellow - 37, cy_yellow), cv2.FONT_HERSHEY_TRIPLEX, 0.48, (0, 0, 0), 1)
        cv2.drawContours(image_yellow, [c], 0, (0, 0, 0), 2)

    light_lower = np.array([0, 0, 220])
    light_upper = np.array([180, 30, 250])
    mask_light_gray = cv2.inRange(hsv_image, light_lower, light_upper)
    detected_light_gray = cv2.bitwise_and(image_light_gray, image_light_gray, mask=mask_light_gray)
    contours_light_gray, _ = cv2.findContours(mask_light_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area_light_gray = 0
    for c in contours_light_gray:
        area_light_gray += cv2.contourArea(c)
        M_light_gray = cv2.moments(c)
        if M_light_gray["m00"] != 0:
            cx_light_gray = int(M_light_gray["m10"] / M_light_gray["m00"])
            cy_light_gray = int(M_light_gray["m01"] / M_light_gray["m00"])
            cv2.putText(original_image, f"{area_light_gray:.2f}", (cx_light_gray - 35, cy_light_gray), cv2.FONT_HERSHEY_TRIPLEX, 0.48, (0, 0, 0), 1)
        cv2.drawContours(image_light_gray, [c], 0, (0, 0, 0), 2)

    gray_lower = np.array([0, 0, 200])
    gray_upper = np.array([220, 0, 250])
    mask_gray = cv2.inRange(hsv_image, gray_lower, gray_upper)
    detected_gray = cv2.bitwise_and(image_gray, image_gray, mask=mask_gray)
    contours_gray, _ = cv2.findContours(mask_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area_gray = 0
    for c in contours_gray:
        area_gray += cv2.contourArea(c)
        M_gray = cv2.moments(c)
        if M_gray["m00"] != 0:
            cx_gray = int(M_gray["m10"] / M_gray["m00"])
            cy_gray = int(M_gray["m01"] / M_gray["m00"])
            cv2.putText(original_image, f"{area_gray:.2f}", (cx_gray - 35, cy_gray), cv2.FONT_HERSHEY_TRIPLEX, 0.48, (0, 0, 0), 1)
        cv2.drawContours(image_gray, [c], 0, (0, 0, 0), 2)

    dark_lower = np.array([0, 0, 100])
    dark_upper = np.array([180, 30, 200])
    mask_dark_gray = cv2.inRange(hsv_image, dark_lower, dark_upper)
    detected_dark_gray = cv2.bitwise_and(image_dark_gray, image_dark_gray, mask=mask_dark_gray)
    contours_dark_gray, _ = cv2.findContours(mask_dark_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area_dark_gray = 0
    for c in contours_dark_gray:
        area_dark_gray += cv2.contourArea(c)
        M_dark_gray = cv2.moments(c)
        if M_dark_gray["m00"] != 0:
            cx_dark_gray = int(M_dark_gray["m10"] / M_dark_gray["m00"])
            cy_dark_gray = int(M_dark_gray["m01"] / M_dark_gray["m00"])
            cv2.putText(original_image, f"{area_dark_gray:.2f}", (cx_dark_gray - 35, cy_dark_gray), cv2.FONT_HERSHEY_TRIPLEX, 0.48, (0, 0, 0), 1)
        cv2.drawContours(image_dark_gray, [c], 0, (0, 0, 0), 2)

    cv2.imshow('Original Image with Area at Centroid', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

pathOfImage = 'fig1.jpg'
calculate_area(pathOfImage) # Perform color detection and area calculation

# Display the original image with area information at the centroid

