import cv2
import mediapipe as mp

kamera=cv2.VideoCapture(0)
cizim=mp.solutions.drawing_utils
el_mod=mp.solutions.hands

with el_mod.Hands(static_image_mode=True) as eller:
    while True:
        ret,frame=kamera.read()
        frame=cv2.flip(frame,1)
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=eller.process(rgb)

        yukseklik,genislik,_=frame.shape

        if result.multi_hand_landmarks:
            for ellandmark in result.multi_hand_landmarks:
                for koordinat in el_mod.HandLandmark:
                    koordinat1 = ellandmark.landmark[4]
                    koordinat2 = ellandmark.landmark[20]
                    cv2.circle(frame, (int(koordinat1.x * genislik), int(koordinat1.y * yukseklik)), 6, (0, 0, 255), -1)
                    cv2.circle(frame, (int(koordinat2.x * genislik), int(koordinat2.y * yukseklik)), 6, (0, 0, 255), -1)

                    cv2.line(frame, (int(koordinat1.x * genislik), int(koordinat1.y * yukseklik)), (int(koordinat2.x * genislik), int(koordinat2.y * yukseklik)),(255,0,0),4)

                    mesafe=int(abs(koordinat2.x-koordinat1.x)*genislik)
                    #print(mesafe)
                    cv2.putText(frame,"Mesafe: "+str(mesafe),(80,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)

                    if mesafe>150:
                        cv2.putText(frame, "Mesafe: " + str(mesafe), (80, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        cv2.imshow("pencere",frame)
        if cv2.waitKey(10) & 0xFF==ord("q"):
            break

kamera.release()
cv2.destroyAllWindows()






