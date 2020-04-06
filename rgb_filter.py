import cv2
import numpy as np

def rgb_filter(image):
    (B,G,R) = cv2.split(image)
    M = np.maximum(np.maximum(B, G), R)
    
    B[B < M] = 0
    G[G < M] = 0
    R[R < M]= 0

    return cv2.merge([B,G,R])