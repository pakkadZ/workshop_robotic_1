import cv2
import mediapipe as mp

checkthumbFinger =""
checkIndexFinger =""
checkMiddleFinger =""
checkRingFinger =""
checkLittleFinger =""
show = ""
Nfing = "non"



cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
tipIds=[3,4,6,8,10,12,16,15,19,20]

while True:
    dot_position=[]
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                dot_position.append([id,cx,cy])
                fingers=[]

            if len(dot_position) !=0:    



               if dot_position[4][1] > dot_position[3][1]:
                 checkthumbFinger ="thumb "
               if dot_position[4][1] < dot_position[3][1]:
                 checkthumbFinger ="" 

               if dot_position[6][2]> dot_position[8][2]:
                 checkIndexFinger ="index "
               if dot_position[6][2]< dot_position[8][2]:
                 checkIndexFinger =""

               if dot_position[10][2]> dot_position[12][2]:
                 checkMiddleFinger ="Middle "
               if dot_position[10][2]< dot_position[12][2]:
                 checkMiddleFinger =""
                
               if dot_position[15][2]> dot_position[16][2]:
                 checkRingFinger ="Ring "
               if dot_position[15][2]< dot_position[16][2]:
                 checkRingFinger =""

               if dot_position[19][2]> dot_position[20][2]:
                 checkLittleFinger="Little "
               if dot_position[19][2]< dot_position[20][2]:
                 checkLittleFinger=""

               
               


                 
                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cv2.putText(img, str("finger:"+checkthumbFinger+checkIndexFinger+checkMiddleFinger+checkRingFinger+checkLittleFinger), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2,
                (100, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)