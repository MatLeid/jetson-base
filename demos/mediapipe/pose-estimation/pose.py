import cv2
import time
import PoseModule as pm
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5065

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open Camera
try:
    default = 0 # Try Changing it to 1 if webcam not found
    cap = cv2.VideoCapture(default)
except:
    print("No Camera Source Found!")

pTime = 0
detector = pm.poseDetector(mode=True)
lastPosY = 0
lastPosX = 0
while cap.isOpened():    
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    
    image = detector.findPose(image)
    lmList = detector.findPosition(image, draw=False)
    if len(lmList) !=0:
        #print(lmList[15])
        cv2.circle(image, (lmList[15][1], lmList[15][2]), 15, (0, 0, 255), cv2.FILLED)
        cv2.circle(image, (lmList[16][1], lmList[16][2]), 15, (255, 0, 255), cv2.FILLED)
        
        #if lmList[16][2] - lastPosY > 20:
         #   print(lmList[16][2]- lastPosY )
          #  lastPosY = lmList[16][2]
          #  sock.sendto( ("JUMP!").encode(), (UDP_IP, UDP_PORT) )

        if lmList[15][2] < 200 or lmList[16][2] < 200:
            print(lmList[15][2],lmList[16][2])
            sock.sendto( ("JUMP!").encode(), (UDP_IP, UDP_PORT) )

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(image, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()