import cv2
import predict
import process
import os
import shutil
import numpy as np
import time
import threading
#import pygame as pg

#pg.init()
#yellow = (255, 255, 0)

#screen = pg.display.set_mode((640, 280))
#pg.display.set_caption("Text adventures with Pygame")
# pick a font you have and set its size
#myfont = pg.font.SysFont("Comic Sans MS", 30)
global stop
stop=0
i=0
answer = ""
camera = cv2.VideoCapture(0)
try:
    os.mkdir('.snaps')
except:
    pass
back_taken=0
def show():
    while stop==0:
            global return_value, image
            return_value, image = camera.read()
            cv2.waitKey(1)
            cv2.imshow("cam",image)
try: 
    while True:
        if back_taken == 0:
            t1 = threading.Thread(target=show)
            t1.start()
            print("Taking Background image in 3 seconds")
            time.sleep(3)
            print("Background Image Taken")
            cv2.imwrite('./.snaps/Background.jpg', image)
            back=cv2.imread('./.snaps/Background.jpg')
            print("Starting the program in 3 seconds")
            for x in range(0,3):
                print(3-x)
                time.sleep(1)
            back_taken=1        
        
        i = i+1
        if(i%4 == 0):
            processedImage = process.process(back=back,image=image)
            cv2.imwrite('./.snaps/opencv'+str(i)+'.jpg', processedImage)
            try:
                prediction = predict.predict('./.snaps/opencv'+str(i)+'.jpg')
                print(prediction)
            except:
                pass
            
            #label = myfont.render(answer, 1, yellow)
            #screen.blit(label, (100, 100))
            # show the whole thing
            #pg.display.flip()
            
            #print("maskOpen-"+prediction2)
            #os.remove('.snaps/opencv'+str(i)+'.jpg')
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
except KeyboardInterrupt:
    pass
try:        
    shutil.rmtree('.snaps')
except:
    pass
stop=1
cv2.destroyAllWindows()
del(camera)
#pg.quit()
#'./.snaps/opencv'+str(i)+'.jpg'
