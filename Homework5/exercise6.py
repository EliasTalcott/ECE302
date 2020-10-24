import cv2
import numpy as np
from matplotlib import pyplot as plt

def plot_image(image, name):
    plt.hist(image.ravel(), 100, [0,1])
    plt.savefig(name)


if __name__ == "__main__":
    # Load image
    img = cv2.imread("Image.jpg", 0)
    # Edit image
    norm_img = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    # Print histograms
    plot_image(norm_img, "Normalized.png")
    # Save image
    cv2.imwrite("ImageEdit.jpg", img)