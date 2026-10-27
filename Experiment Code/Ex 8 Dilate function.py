import cv2
import numpy as np
image = cv2.imread("C:/Users/dhars/OneDrive/Pictures/Photo/images.jpg")
if image is None:
    print("Error: Could not read the image.")
else:
    cv2.imshow("Original Image", image)
    kernel = np.ones((5, 5), np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=1)
    cv2.imshow("Dilated Image", dilated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
