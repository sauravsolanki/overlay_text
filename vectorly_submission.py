#####################
import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8)
    # convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
    
    # make a mask based on threshold
    _,thresh = cv2.threshold(gray,0,160,cv2.THRESH_BINARY_INV) 

    # define and dilate the thresholded images
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 15) # dilate

    # Black <----> white
    dilated = (255 - dilated)

    # taking 150 as threshold, coverting below it to black and above it to white
    dilated[dilated >= 150] = 255
    dilated[dilated < 150] = 0

    return  dilated

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
