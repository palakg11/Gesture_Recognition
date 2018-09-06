import cv2
import os
import shutil
import numpy as np
import time
import threading

global stop
stop=0
i=0

try:
    os.mkdir('3')
except:
    pass
camera = cv2.VideoCapture(0)
def show():
    while stop==0:
            global return_value, image
            return_value, image = camera.read()
            cv2.waitKey(1)
            cv2.imshow("cam",image)
t1 = threading.Thread(target=show)
t1.start()
print("Taking Background image in 3 seconds")
time.sleep(3)
cv2.imwrite('./3/Background.jpg', image)
print("Background Image Taken")
print("Starting to take object images in 3 seconds")
for x in range(0,3):
    print(3-x)
    time.sleep(1)
try: 
    while True:
        i = i+1
        if(i%4 == 0):
            cv2.imwrite('./3/opencv'+str(i)+'.jpg', image)           

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
except KeyboardInterrupt:
    pass
stop=1
cv2.destroyAllWindows()
del(camera)

