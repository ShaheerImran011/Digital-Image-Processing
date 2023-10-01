# import cv2

# def is_blurred(image_path1, image_path2):
#     # Load the two grayscale images
#     image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
#     image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)
    
#     # Calculate the variance of Laplacian for each image
#     sharpness1 = cv2.Laplacian(image1, cv2.CV_64F).var()
#     sharpness2 = cv2.Laplacian(image2, cv2.CV_64F).var()
    
#     # Determine which image is blurred based on sharpness
#     if sharpness1 < sharpness2:
#         return "Blurred Image", "Original Image"
#     else:
#         return "Original Image", "Blurred Image"

# # Test the function with your image pairs
# original_image_path = "fig5.jpg"  # Replace with the path to your original image
# blurred_image_path = "fig5_blur.jpg"    # Replace with the path to your blurred image

# sharp_image, blurred_image = is_blurred(original_image_path, blurred_image_path)

# # Display the images with titles
# original_image = cv2.imread(original_image_path)
# blurred_image = cv2.imread(blurred_image_path)

# cv2.imshow("Original Image", original_image)
# cv2.imshow("Blurred Image", blurred_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import cv2

def is_blurred(image_path1, image_path2):
    image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)
    
    sharpness1 = cv2.Laplacian(image1, cv2.CV_64F).var()
    sharpness2 = cv2.Laplacian(image2, cv2.CV_64F).var()
    
    if sharpness1 < sharpness2:
        return "Blurred Image", "Original Image"
    else:
        return "Original Image", "Blurred Image"

original_image_path = "fig5.jpg"
blurred_image_path = "fig5_blur.jpg"

sharp_image, blurred_image = is_blurred(original_image_path, blurred_image_path)

original_image = cv2.imread(original_image_path)
blurred_image = cv2.imread(blurred_image_path)

cv2.imshow("Original Image", original_image)
cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# The code compares the sharpness of two images and determines which one is blurred.
# It then displays both images with appropriate titles.

