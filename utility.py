import cv2
import numpy as np
import argparse

# Rgb filter


def rgb_filter(image):
    (B, G, R) = cv2.split(image)
    M = np.maximum(np.maximum(B, G), R)

    B[B < M] = 0
    G[G < M] = 0
    R[R < M] = 0

    return cv2.merge([B, G, R])

# translate function


def translate(image, x, y):
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
    return shifted

# rotate function


def rotate(image, angle, centre=None, scale=1.0):
    (h, w) = image.shape[:2]

    if centre = None:
        centre = (w//2, h//2)

    matrix = cv2.getRotationMatrix2D(centre, angle, scale)
    rotated = cv2.warpAffine(image, matrix, (w, h))
    return rotated

# resize function


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image

    if height is None:
        r = width / float(w)
        dim = (width, int(h*r))
    else:
        r = height / float(h)
        dim = (int(r * width), height)

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

# #flipping function
# def flip(image, vertical=False, horizontal=False, inverted=False):
#     if vertical is True:
#        return cv2.flip(image, 0)
#     elif horizontal is True:
#       return cv2.flip(image, 1)
#     elif inverted is True:
#       return cv2.flip(image, -1)
