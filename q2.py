# import cv2
# import numpy as np

# def detect_gender(image_path):
#     # Load the image
#     image = cv2.imread(image_path)
    
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # Threshold the image to create a binary mask
#     _, binary_mask = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    
#     # Find contours in the binary mask
#     contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Calculate the aspect ratio of the largest contour
#     aspect_ratios = [cv2.contourArea(contour) for contour in contours]
#     if aspect_ratios:
#         max_aspect_ratio = max(aspect_ratios)
#     else:
#         max_aspect_ratio = 0
    
#     # Determine the gender based on aspect ratio
#     if max_aspect_ratio > 1.174736842105263:  # Adjust this threshold based on your images
#         return "Girl"
#     else:
#         return "Boy"

# # Test the function with your images
# left_image_path = "fig3.jpg"  # Replace with the path to your left image
# right_image_path = "fig4.jpg"  # Replace with the path to your right image

# left_gender = detect_gender(left_image_path)
# right_gender = detect_gender(right_image_path)

# print("Left image is a:", left_gender)
# print("Right image is a:", right_gender)






# import cv2
# import numpy as np

# def detect_gender(image_path):
#     # Load the image
#     image = cv2.imread(image_path)
    
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # Use Canny edge detection to highlight edges
#     edges = cv2.Canny(gray, 50, 150)
    
#     # Use Hough Line Transform to detect lines (hairlines)
#     lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)
    
#     if lines is not None:
#         # Count the number of horizontal lines (hairlines)
#         horizontal_lines = 0
#         vertical_lines = 0
#         for line in lines:
#             x1, y1, x2, y2 = line[0]
#             if abs(y2 - y1) > abs(x2 - x1):
#                 horizontal_lines += 1
#             else:
#                 vertical_lines += 1
        
#         # Determine the gender based on the number of horizontal lines
#         if horizontal_lines > vertical_lines:
#             return "Girl"
#         else:
#             return "Boy"
#     else:
#         return "Unknown"

# # Test the function with your images
# left_image_path = "fig3.jpg"  # Replace with the path to your left image
# right_image_path = "fig4.jpg"  # Replace with the path to your right image

# left_gender = detect_gender(left_image_path)
# right_gender = detect_gender(right_image_path)

# print("Left image is a:", left_gender)
# print("Right image is a:", right_gender)




import cv2

def detect_gender(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use Canny edge detection to highlight edges
    edges = cv2.Canny(gray, 50, 150)
    
    # Find contours in the Canny edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Initialize variables to keep track of hairline lengths
    total_hairline_length = 0
    hairline_count = 0
    
    # Calculate the hairline length for each contour
    for contour in contours:
        # Filter out small contours (noise)
        if cv2.contourArea(contour) < 100:
            continue
        
        # Calculate the hairline length as the sum of all contour arc lengths
        hairline_length = cv2.arcLength(contour, closed=True)
        total_hairline_length += hairline_length
        hairline_count += 1
    
    # Calculate the average hairline length
    if hairline_count > 0:
        average_hairline_length = total_hairline_length / hairline_count
    else:
        average_hairline_length = 0
    
    # Determine the gender based on the average hairline length
    if average_hairline_length > 300:  # Adjust this threshold based on your images
        return "Girl"
    else:
        return "Boy"

# Test the function with your images
left_image_path = "fig3.jpg"  # Replace with the path to your left image
right_image_path = "fig4.jpg"  # Replace with the path to your right image

left_gender = detect_gender(left_image_path)
right_gender = detect_gender(right_image_path)

print("Left image is a:", left_gender)
print("Right image is a:", right_gender)

