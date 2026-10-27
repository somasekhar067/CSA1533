import cv2

# Read the image
image = cv2.imread("C:/Users/dhars/OneDrive/Pictures/Photo/images.jpg")

# Check if image is loaded
if image is None:
    print("Error: Could not read the image.")
else:
    # Display original image
    cv2.imshow("Original Image", image)

    # Create a kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # Apply erosion
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Display eroded image
    cv2.imshow("Eroded Image", eroded_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
