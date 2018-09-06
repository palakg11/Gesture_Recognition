import cv2
import numpy as np
import os

x=1
while(True):
    
    back = cv2.imread('CreatedData/'+str(x)+'/Background.jpg')
    try:
        if back == None:
            break
    except:
        pass
    try:
        os.mkdir('TrainingSet/'+str(x))
    except:
        pass
    y=4
    while(True):

        obj = cv2.imread('CreatedData/'+str(x)+'/opencv'+str(y)+'.jpg')
        try:
            if obj == None:
                break
        except:
            pass
        for i in range(0,480):
            for j in range(0,640):
                r1 = int(back[i][j][0])
                g1 = int(back[i][j][1])
                b1 = int(back[i][j][2])
                r2 = int(obj[i][j][0])
                g2 = int(obj[i][j][1])
                b2 = int(obj[i][j][2])
                if r1-r2 <= 13 and r1>=r2:
                    if g1-g2 <=18 and g1>=g2:
                        if b1-b2 <=23 and b1>=b2:
                            r2=0
                            g2=0
                            b2=0
                        if b2-b1 <=23 and b2>=b1:
                            r2=0
                            g2=0
                            b2=0
                    if g2-g1 <=18 and g2>=g1:
                        if b1-b2 <=23 and b1>=b2:
                            r2=0
                            g2=0
                            b2=0
                        if b2-b1 <=23 and b2>=b1:
                            r2=0
                            g2=0
                            b2=0
                    if b1-b2 <=18 and b1>=b2:
                        if g1-g2 <=23 and g1>=g2:
                            r2=0
                            g2=0
                            b2=0
                        if g2-g1 <=23 and g2>=g1:
                            r2=0
                            g2=0
                            b2=0
                    if b2-b1 <=18 and b2>=b1:
                        if g1-g2 <=23 and g1>=g2:
                            r2=0
                            g2=0
                            b2=0
                        if g2-g1 <=23 and g2>=g1:
                            r2=0
                            g2=0
                            b2=0

                if r2-r1 <= 13 and r2>=r1:
                    if g1-g2 <=18 and g1>=g2:
                        if b1-b2 <=23 and b1>=b2:
                            r2=0
                            g2=0
                            b2=0
                        if b2-b1 <=23 and b2>=b1:
                            r2=0
                            g2=0
                            b2=0
                    if g2-g1 <=18 and g2>=g1:
                        if b1-b2 <=23 and b1>=b2:
                            r2=0
                            g2=0
                            b2=0
                        if b2-b1 <=23 and b2>=b1:
                            r2=0
                            g2=0
                            b2=0
                    if b1-b2 <=18 and b1>=b2:
                        if g1-g2 <=23 and g1>=g2:
                            r2=0
                            g2=0
                            b2=0
                        if g2-g1 <=23 and g2>=g1:
                            r2=0
                            g2=0
                            b2=0
                    if b2-b1 <=18 and b2>=b1:
                        if g1-g2 <=23 and g1>=g2:
                            r2=0
                            g2=0
                            b2=0
                        if g2-g1 <=23 and g2>=g1:
                            r2=0
                            g2=0
                            b2=0

                if g1-g2 <= 13 and g1>=g2:
                    if r1-r2 <=18 and r1>=r2:
                        if b1-b2 <=23 and b1>=b2:
                            r2=0
                            g2=0
                            b2=0
                        if b2-b1 <=23 and b2>=b1:
                            r2=0
                            g2=0
                            b2=0
                    if r2-r1 <=18 and r2>=r1:
                        if b1-b2 <=23 and b1>=b2:
                            r2=0
                            g2=0
                            b2=0
                        if b2-b1 <=23 and b2>=b1:
                            r2=0
                            g2=0
                            b2=0
                    if b1-b2 <=18 and b1>=b2:
                        if r1-r2 <=23 and r1>=r2:
                            r2=0
                            g2=0
                            b2=0
                        if r2-r1 <=23 and r2>=r1:
                            r2=0
                            g2=0
                            b2=0
                    if b2-b1 <=18 and b2>=b1:
                        if r1-r2 <=23 and r1>=r2:
                            r2=0
                            g2=0
                            b2=0
                        if r2-r1 <=23 and r2>=r1:
                            r2=0
                            g2=0
                            b2=0

                if g2-g1 <= 13 and g2>=g1:
                    if r1-r2 <=18 and r1>=r2:
                        if b1-b2 <=23 and b1>=b2:
                            r2=0
                            g2=0
                            b2=0
                        if b2-b1 <=23 and b2>=b1:
                            r2=0
                            g2=0
                            b2=0
                    if r2-r1 <=18 and r2>=r1:
                        if b1-b2 <=23 and b1>=b2:
                            r2=0
                            g2=0
                            b2=0
                        if b2-b1 <=23 and b2>=b1:
                            r2=0
                            g2=0
                            b2=0
                    if b1-b2 <=18 and b1>=b2:
                        if r1-r2 <=23 and r1>=r2:
                            r2=0
                            g2=0
                            b2=0
                        if r2-r1 <=23 and r2>=r1:
                            r2=0
                            g2=0
                            b2=0
                    if b2-b1 <=18 and b2>=b1:
                        if r1-r2 <=23 and r1>=r2:
                            r2=0
                            g2=0
                            b2=0
                        if r2-r1 <=23 and r2>=r1:
                            r2=0
                            g2=0
                            b2=0

                if b1-b2 <= 13 and b1>=b2:
                    if r1-r2 <=18 and r1>=r2:
                        if g1-g2 <=23 and g1>=g2:
                            r2=0
                            g2=0
                            b2=0
                        if g2-g1 <=23 and g2>=g1:
                            r2=0
                            g2=0
                            b2=0
                    if r2-r1 <=18 and r2>=r1:
                        if g1-g2 <=23 and g1>=g2:
                            r2=0
                            g2=0
                            b2=0
                        if g2-g1 <=23 and g2>=g1:
                            r2=0
                            g2=0
                            b2=0
                    if g1-g2 <=18 and r1>=r2:
                        if r1-r2 <=23 and r1>=r2:
                            r2=0
                            g2=0
                            b2=0
                        if r2-r1 <=23 and r2>=r1:
                            r2=0
                            g2=0
                            b2=0
                    if g2-g1 <=18 and r2>=r1:
                        if r1-r2 <=23 and r1>=r2:
                            r2=0
                            g2=0
                            b2=0
                        if r2-r1 <=23 and r2>=r1:
                            r2=0
                            g2=0
                            b2=0

                if b2-b1 <= 13 and b2>=b1:
                    if r1-r2 <=18 and r1>=r2:
                        if g1-g2 <=23 and g1>=g2:
                            r2=0
                            g2=0
                            b2=0
                        if g2-g1 <=23 and g2>=g1:
                            r2=0
                            g2=0
                            b2=0
                    if r2-r1 <=18 and r2>=r1:
                        if g1-g2 <=23 and g1>=g2:
                            r2=0
                            g2=0
                            b2=0
                        if g2-g1 <=23 and g2>=g1:
                            r2=0
                            g2=0
                            b2=0
                    if g1-g2 <=18 and g1>=g2:
                        if r1-r2 <=23 and r1>=r2:
                            r2=0
                            g2=0
                            b2=0
                        if r2-r1 <=23 and r2>=r1:
                            r2=0
                            g2=0
                            b2=0
                    if g2-g1 <=18 and g2>=g1:
                        if r1-r2 <=23 and r1>=r2:
                            r2=0
                            g2=0
                            b2=0
                        if r2-r1 <=23 and r2>=r1:
                            r2=0
                            g2=0
                            b2=0

                obj[i][j][0]=r2
                obj[i][j][1]=g2
                obj[i][j][2]=b2
                    

        cv2.imwrite('TrainingSet/'+str(x)+'/opencv'+str(y)+'.jpg',obj)
        y+=4
    x=x+1

