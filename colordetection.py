# import cv2
# from PIL import Image
# from utils import get_limits

# black=[0,0,0]
# cap=cv2.VideoCapture(0)
# while True:
#   ret,frame=cap.read()
#   hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#   lowerlimit,upperlimit=get_limits(color=black)
#   mask=cv2.inRange(hsvImage,lowerlimit,upperlimit)
#   mask_=Image.fromarray(mask)
#   bbox=mask_.getbbox()
#   if bbox is not None:
#     x1,y1,x2,y2=bbox
#     cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),4)
#   cv2.imshow("frame",mask)
#   if cv2.waitKey(1)& 0XFF==ord('q'):
#       cap.release()
#       cv2.destroyAllWindows()
import cv2
from PIL import Image
import numpy as np

# Define the color to detect (black in this case)
black = [0, 0, 0]

# Function to get HSV limits for a given BGR color
def get_limits(color):
    c = np.uint8([[color]])  # Convert color to a NumPy array
    hsvc = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)  # Convert the color to HSV
    lowerlimit = (hsvc[0][0][0] - 10, 100, 100)
    upperlimit = (hsvc[0][0][0] + 10, 255, 255)
    
    # Use uint8 instead of uint32 for the inRange function
    lowerlimit = np.array(lowerlimit, dtype=np.uint8)
    upperlimit = np.array(upperlimit, dtype=np.uint8)
    
    return lowerlimit, upperlimit

# Initialize webcam video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Capture frame from webcam
    if not ret:
        break
    
    # Convert frame from BGR to HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get the lower and upper limits for the black color in HSV
    lowerlimit, upperlimit = get_limits(color=black)
    
    # Create a mask where the detected color is within the limits
    mask = cv2.inRange(hsvImage, lowerlimit, upperlimit)
    
    # Convert the mask to a PIL image to find the bounding box (bbox)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    
    # If a bbox is found, draw a rectangle around the detected area
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
    
    # Display the masked frame
    cv2.imshow("frame", frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
