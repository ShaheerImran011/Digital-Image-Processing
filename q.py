# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('rect1.jpg')

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Threshold the image to create a binary mask for white objects
# _, binary_mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# # Find contours in the binary mask
# contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Initialize variables to store the largest rectangle or square
# largest_area = 0
# largest_contour = None

# # Iterate through the contours to find the largest rectangle or square
# for contour in contours:
#     # Approximate the contour to a polygon
#     epsilon = 0.04 * cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, epsilon, True)
    
#     # Check if the polygon has 4 corners (a rectangle or square)
#     if len(approx) == 4:
#         # Calculate the area of the polygon
#         area = cv2.contourArea(approx)
        
#         # If it's the largest area so far, update the variables
#         if area > largest_area:
#             largest_area = area
#             largest_contour = approx

# # If a rectangle or square is found, calculate the perimeter and centroid
# if largest_contour is not None:
#     perimeter = cv2.arcLength(largest_contour, True)
#     M = cv2.moments(largest_contour)
#     centroid_x = int(M['m10'] / M['m00'])
#     centroid_y = int(M['m01'] / M['m00'])
    
#     # Display the results
#     print("Parameter (Perimeter):", perimeter)
#     print("Centroid (x, y):", centroid_x, centroid_y)
# else:
#     print("No rectangle or square found in the image.")

# # Display the image with the detected contour
# cv2.drawContours(image, [largest_contour], -1, (0, 255, 0), 2)
# cv2.imshow('Detected Object', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import cv2
import numpy as np

image = cv2.imread('rect1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

largest_area = 0
largest_contour = None

for contour in contours:
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    if len(approx) == 4:
        area = cv2.contourArea(approx)
        
        if area > largest_area:
            largest_area = area
            largest_contour = approx

if largest_contour is not None:
    perimeter = cv2.arcLength(largest_contour, True)
    M = cv2.moments(largest_contour)
    centroid_x = int(M['m10'] / M['m00'])
    centroid_y = int(M['m01'] / M['m00'])
    
    print("Parameter (Perimeter):", perimeter)
    print("Centroid (x, y):", centroid_x, centroid_y)
else:
    print("No rectangle or square found in the image.")

cv2.drawContours(image, [largest_contour], -1, (0, 255, 0), 2)
cv2.imshow('Detected Object', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# The code detects the largest rectangle or square in the input image,
# calculates its perimeter and centroid, and displays the image with the detected contour.

