import numpy as np


# Used only once to be sure that all images are gray
# Used on gray rgb images
# Runtime ~5 minutes
def is_grayscale(images):
    is_gray = True
    for image in images:
        for line in image:
            for elem in line:
                if np.all(elem != elem[0]):
                    is_gray = False
    return is_gray
