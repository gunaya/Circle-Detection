# python color_tracking.py --video balls.mp4
# python color_tracking.py

# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import urllib  # for reading image from URL

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
                help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the colors in the HSV color space
lower = {'red': (166, 84, 141), 'green': (66, 122, 129), 'blue': (97, 100, 117), 'yellow': (23, 59, 119),
         'orange': (0, 50, 80)}  # assign new item lower['blue'] = (93, 10, 0)
upper = {'red': (186, 255, 255), 'green': (86, 255, 255), 'blue': (117, 255, 255), 'yellow': (54, 255, 255),
         'orange': (20, 255, 255)}

# define standard colors for circle around the object
colors = {'red': (0, 0, 255), 'green': (0, 255, 0), 'blue': (255, 0, 0), 'yellow': (0, 255, 217),
          'orange': (0, 140, 255)}

# pts = deque(maxlen=args["buffer"])

# if a video path was not supplied, grab the reference
# to the webcam
# if not args.get("video", False):
#     camera = cv2.VideoCapture(1)
# # otherwise, grab a reference to the video file
# else:
#     camera = cv2.VideoCapture(args["video"])
# # keep looping
# while True:
#     # grab the current frame
#     (grabbed, frame) = camera.read()
#     # if we are viewing a video and we did not grab a frame,
#     # then we have reached the end of the video
#     if args.get("video") and not grabbed:
#         break

image = cv2.imread('fruit3.jpg')
# image = cv2.imread('green.jpg')    #kkuning param2=100
# image = cv2.imread('fruit.jpg')    #biru dan oranye
# image = cv2.imread('ball.jpg')     #terdeteksi oranye dan kuning
# image = cv2.imread('ima.jpeg')     #terdeteksi merah dan kuning
# image = cv2.imread('fruit2.jpg')   #terdeteksi hijau
# image = cv2.imread('ima1.jpeg')    #koin oranye param2=150

# resize the frame, blur it, and convert it to the HSV
# color space
frame = imutils.resize(image, width=600)

blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

# for each color in dictionary check object in frame
for key, value in upper.items():

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.inRange(hsv, lower[key], upper[key])

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    im2, contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    im2 = cv2.GaussianBlur(mask, (9, 9), 0)
    im2 = cv2.Canny(im2, 300, 400)
    print("Dideteksi Sebanyak " + str(len(contours)) + " Contour " + key)

    circles = cv2.HoughCircles(im2, cv2.HOUGH_GRADIENT, 2, 145, param1=200, param2=120, minRadius=0,
                               maxRadius=300)
    if circles is None:
        cv2.imshow("Frame", frame)
    else:
        i = 0
        circles = np.round(circles[0, :].astype("int"))
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, colors[key], 4)
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

            cv2.putText(frame, key, (int(x - r), int(y - r)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        colors[key], 2)
            # cv2.putText(imOutput, pixelString, (x, y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), lineType=50)
            # cv2.imshow("output", np.hstack([image, imOutput]))
            # cv2.imshow("ouput", frame)
            i += 1
        print("Dideteksi Sebanyak " + str(i) + " Lingkaran " + key)

# show the frame to our screen
        cv2.imshow("Frame", frame)

key = cv2.waitKey(0) & 0xFF
# if the 'q' key is pressed, stop the loop
if key == ord("q"):
    # break

# cleanup the camera and close any open windows
# camera.release()
    cv2.destroyAllWindows()