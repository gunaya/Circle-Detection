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
ap.add_argument("-i", "--image",
                help="path to the (optional) image file")
args = vars(ap.parse_args())

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

# IP webcam image stream
# URL = 'http://10.254.254.102:8080/shot.jpg'
# urllib.urlretrieve(URL, 'shot1.jpg')

def identifikasi(image):
    frame = image
    frame = imutils.resize(frame, width=600)

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # for each color in dictionary check object in frame
    for key, value in upper.items():

        kernel = np.ones((9, 9), np.uint8)
        mask = cv2.inRange(hsv, lower[key], upper[key])
        cv2.imshow("t", mask)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cv2.imshow("opening", mask)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("closing", mask)
        im2, contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                                    cv2.CHAIN_APPROX_SIMPLE)

        cv2.imshow("contours", im2)
        im2 = cv2.GaussianBlur(mask, (9,9),0)
        cv2.imshow("Blur", im2)
        im2 = cv2.Canny(im2, 200, 400)
        cv2.imshow("Tepi", im2)
        print("Dideteksi Sebanyak " + str(len(contours)) + " Contour " + key)

        circles = cv2.HoughCircles(im2, cv2.HOUGH_GRADIENT, 2, 145, param1=200, param2=100, minRadius=0,
                                   maxRadius=1000)
        if circles is None:
            print("Circle not detected")
            return frame
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
                i +=1
            print("Dideteksi Sebanyak " + str(i) + " Lingkaran " + key)
            return frame
    # cv2.imshow("a",img)

# image = cv2.imread('images/eye2.jpg')     #biru
# image = cv2.imread('images/green.jpg')    #kkuning param2=100
# image = cv2.imread('images/fruit.jpg')    #biru dan oranye
# image = cv2.imread('images/ball.jpg')     #terdeteksi oranye dan kuning
# image = cv2.imread('images/ima.jpeg')     #terdeteksi merah dan kuning
# image = cv2.imread('images/fruit2.jpg')   #terdeteksi hijau
# image = cv2.imread('images/ima1.jpeg')    #koin oranye param2=150
image = cv2.imread('images/fruit3.jpg')

print("MASUKKAN INPUT")
print("[M]erah, [H]ijau, [B]iru, [K]uning, [O]ranye")

key = input('masukkan input : ').lower()
if key == 'm':
    lower = {'Merah': (166, 84, 141)}  # assign new item lower['blue'] = (93, 10, 0)
    upper = {'Merah': (186, 255, 255)}

    # define standard colors for circle around the object
    colors = {'Merah': (0, 0, 255)}
    frame = identifikasi(image)
    # frame = imutils.resize(frame, width=600)
    cv2.imshow("a",frame)
    wait = cv2.waitKey(0)
    if wait == ord('q'):
        cv2.destroyAllWindows()

elif key == 'h':
    lower = {'Hijau': (66, 122, 129)}
    upper = {'Hijau': (86, 255, 255)}

    # define standard colors for circle around the object
    colors = {'Hijau': (0, 255, 0)}

    frame = identifikasi(image)
    cv2.imshow("a",frame)
    wait = cv2.waitKey(0)
    if wait == ord('q'):
        cv2.destroyAllWindows()

elif key == 'b':
    lower = {'Biru': (97, 100, 117)}  # assign new item lower['blue'] = (93, 10, 0)
    upper = {'Biru': (117, 255, 255)}

    # define standard colors for circle around the object
    colors = {'Biru': (255, 0, 0)}
    frame = identifikasi(image)
    cv2.imshow("a",frame)
    wait = cv2.waitKey(0)
    if wait == ord('q'):
        cv2.destroyAllWindows()

elif key == 'k':
    lower = {'Kuning': (23, 59, 119)}  # assign new item lower['blue'] = (93, 10, 0)
    upper = {'Kuning': (54, 255, 255)}

    # define standard colors for circle around the object
    colors = {'Kuning': (0, 255, 217)}
    frame = identifikasi(image)
    cv2.imshow("a",frame)
    wait = cv2.waitKey(0)
    if wait == ord('q'):
        cv2.destroyAllWindows()

elif key == 'o':
    lower = {'Orange': (0, 50, 80)}  # assign new item lower['blue'] = (93, 10, 0)
    upper = {'Orange': (20, 255, 255)}

    # define standard colors for circle around the object
    colors = {'Orange': (0, 140, 255)}
    frame = identifikasi(image)
    cv2.imshow("a",frame)
    wait = cv2.waitKey(0)
    if wait == ord('q'):
        cv2.destroyAllWindows()

else:
    cv2.destroyAllWindows()