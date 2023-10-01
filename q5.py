# import cv2
# import numpy as np

# def calculate_area_with_arrow(image_path):
#     original_image = cv2.imread(image_path)
#     hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

#     # Define the color range for the red arrow
#     red_lower = np.array([0, 100, 100])
#     red_upper = np.array([10, 255, 255])
#     mask_red = cv2.inRange(hsv_image, red_lower, red_upper)
#     red_contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Calculate the total area of the red arrow
#     total_red_area = 0
#     for c in red_contours:
#         total_red_area += cv2.contourArea(c)

#     # Define color ranges for the bars (yellow, light gray, gray, dark gray)
#     color_ranges = [
#         ((20, 100, 100), (30, 255, 255)),  # Yellow
#         ((0, 0, 220), (180, 30, 250)),    # Light Gray
#         ((0, 0, 200), (220, 0, 250)),    # Gray
#         ((0, 0, 100), (180, 30, 200))    # Dark Gray
#     ]

#     # Calculate the area of each bar covered by the red arrow
#     print("Bar Area Covered(%)")
#     for color_range in color_ranges:
#         lower, upper = color_range
#         mask = cv2.inRange(hsv_image, np.array(lower), np.array(upper))
#         bar_contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         bar_area = 0
#         for c in bar_contours:
#             bar_area += cv2.contourArea(c)

#         # Calculate the percentage area covered by the red arrow
#         percentage_covered = (bar_area / total_red_area) * 100
#         color_name = "Yellow" if color_range == color_ranges[0] else \
#                      "Light Gray" if color_range == color_ranges[1] else \
#                      "Gray" if color_range == color_ranges[2] else "Dark Gray"
        
#         print(f"{color_name}: {percentage_covered:.2f}%")

#         # Display the image with annotations
#     cv2.imshow('Image with Percentage Area Covered by Red Arrow', original_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # Replace 'image_path' with the path to your image
# image_path = 'fig2.jpg'
# calculate_area_with_arrow(image_path)


import cv2
import numpy as np

def calculate_area_with_arrow(image_path):
    original_image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

    # Define the color range for the red arrow
    red_lower = np.array([0, 100, 100])
    red_upper = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv_image, red_lower, red_upper)
    red_contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate the total area of the red arrow
    total_red_area = 0
    for c in red_contours:
        total_red_area += cv2.contourArea(c)

    # Define color ranges for the bars (yellow, light gray, gray, dark gray)
    color_ranges = [
        ((20, 100, 100), (30, 255, 255)),  # Yellow
        ((0, 0, 220), (180, 30, 250)),    # Light Gray
        ((0, 0, 200), (220, 0, 250)),    # Gray
        ((0, 0, 100), (180, 30, 200))    # Dark Gray
    ]

    # Calculate the area of each bar covered by the red arrow
    for color_range in color_ranges:
        lower, upper = color_range
        mask = cv2.inRange(hsv_image, np.array(lower), np.array(upper))
        bar_contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        bar_area = 0
        for c in bar_contours:
            bar_area += cv2.contourArea(c)

        # Calculate the percentage area covered by the red arrow
        percentage_covered = (bar_area / total_red_area) * 100
        color_name = "Yellow" if color_range == color_ranges[0] else \
                     "Light Gray" if color_range == color_ranges[1] else \
                     "Gray" if color_range == color_ranges[2] else "Dark Gray"
        
        # Display the percentage on the image
        cv2.putText(original_image, f"{color_name}: {percentage_covered:.2f}%", (10, 30 * (color_ranges.index(color_range) + 1)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the image with annotations
    cv2.imshow('Image with Percentage Area Covered by Red Arrow', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Replace 'image_path' with the path to your image
image_path = 'fig2.jpg'
calculate_area_with_arrow(image_path)
