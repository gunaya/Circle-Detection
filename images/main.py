import cv2
import numpy as np
import argparse


# ===================================================================================================================
# image = cv2.imread('images/logo.png',1)
# cv2.imshow('image',image)
#
# k = cv2.waitKey(0)
# if k == 27:
#     print("closing")
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('images/results/logogray.png',image)
#     print("saving")
#     cv2.destroyAllWindows()
# ===================================================================================================================

#argument parser, load image from command line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Image Path")
args = vars(ap.parse_args())

#load image
image = cv2.imread(args["image"])
imOutput = image.copy()

imGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imCanny = cv2.Canny(imGray, 200, 300)
# cv2.imshow("canny", imCanny)

imGray = cv2.medianBlur(imGray,5)
circles = cv2.HoughCircles(imGray, cv2.HOUGH_GRADIENT, 2, 145, param1=110, param2=120, minRadius=0, maxRadius=200)
# circles = cv2.HoughCircles(imGray, cv2.HOUGH_GRADIENT, 1.2, 100)

if circles is not None:
    circles = np.round(circles[0, :].astype("int"))
    i = 1
    for(x, y, r) in circles:
        cv2.circle(imOutput, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(imOutput, (x-5, y-5), (x+5, y+5), (0, 128, 255), -1)
        pixel = image[y, x]
        string = str(i)
        pixelString = str(pixel)

        print("lingkaran ke -"+string+". Warna :"+pixelString)
        cv2.putText(imOutput, string, (x, y-25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), lineType=50)
        # cv2.putText(imOutput, pixelString, (x, y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), lineType=50)
        i += 1

    # cv2.imshow("output", np.hstack([image, imOutput]))
    cv2.imshow("ouput", imOutput)
    # print(len(circles))
    cv2.waitKey(0)
else:
    print("circle not found")

