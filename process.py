import cv2
import numpy as np

def process(back, image):

    for i in range(0,480):
        for j in range(0,640):
            r1 = int(back[i][j][0])
            g1 = int(back[i][j][1])
            b1 = int(back[i][j][2])
            r2 = int(image[i][j][0])
            g2 = int(image[i][j][1])
            b2 = int(image[i][j][2])
            if r1-r2 <= 9 and r1-r2>=-9:
                if g1-g2 <=14 and g1-g2>=-14:
                    if b1-b2 <=18 and b1-b2>=-18:
                        r2=0
                        g2=0
                        b2=0
                if b1-b2 <=14 and b1-b2>=-14:
                    if g1-g2 <=18 and g1-g2>=-18:
                        r2=0
                        g2=0
                        b2=0

            if g1-g2 <= 9 and g1-g2>=-9:
                if r1-r2 <=14 and r1-r2>=-14:
                    if b1-b2 <=18 and b1-b2>=-18:
                        r2=0
                        g2=0
                        b2=0
                if b1-b2 <=14 and b1-b2>=-14:
                    if r1-r2 <=18 and r1-r2>=-18:
                        r2=0
                        g2=0
                        b2=0

            if b1-b2 <= 9 and b1-b2>=-9:
                if r1-r2 <=14 and r1-r2>=-14:
                    if g1-g2 <=18 and g1-g2>=-18:
                        r2=0
                        g2=0
                        b2=0
                if g1-g2 <=14 and g1-g2>=-14:
                    if r1-r2 <=18 and r1-r2>=-18:
                        r2=0
                        g2=0
                        b2=0

            image[i][j][0]=r2
            image[i][j][1]=g2
            image[i][j][2]=b2

            if j%5 == 0 or i%5 == 0:
                try:
                    if int(image[i][j][0]) == 0 and int(image[i][j-5][0])==0:
                        for k in range (1,5):
                            image[i][j-k][0]=0
                            image[i][j-k][1]=0
                            image[i][j-k][2]=0
                    
                    if int(image[i][j][0]) == 0 and int(image[i-5][j][0])==0:
                        for k in range (1,5):
                            image[i-k][j][0]=0
                            image[i-k][j][1]=0
                            image[i-k][j][2]=0
                    
                        
                except:
                    pass
                

    return image

