import cv2
import numpy as np

def get_limits(color):
  c=np.uint8([[color]])
  hsvc=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
  lowerlimit=hsvc[0][0][0]-10,100,100
  upperlimit=hsvc[0][0][0]+10,255,255
  lowerlimit=np.array(lowerlimit,dtype=np.uint32)
  upperlimit=np.array(upperlimit,dtype=np.uint32)
  return lowerlimit,upperlimit