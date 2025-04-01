from djitellopy import tello
import cv2

nav=tello.Tello()
nav.connect()
print(nav.get_battery())

nav.streamon ()

while True:
    img = nav.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
