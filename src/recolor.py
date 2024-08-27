import cv2
import numpy as np
import os

def detect_and_replace_red(image_path, output_path):
    image = cv2.imread(image_path)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([25, 255, 255])
    lower_red2 = np.array([160, 50, 50])
    upper_red2 = np.array([179, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 | mask2

    hsv[mask > 0] = [30, 255, 255]
    hsv[np.logical_and(mask > 0, hsv[:, :, 2] < 128)] = [30, 255, 255]

    output_path = output_path + "/" + os.path.basename(image_path)

    output_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imwrite(output_path, output_image)

    print(f"Image saved to {output_path}")