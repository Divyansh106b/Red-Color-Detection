import cv2
import numpy as np 

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    if not ret:
        print("CANNOT CAPTURE")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

 
    lower_value_red1 = np.array([0, 120, 70])
    upper_value_red1 = np.array([10, 255, 255])
    lower_value_red2 = np.array([170, 120, 70])
    upper_value_red2 = np.array([180, 255, 255])

 
    red_1 = cv2.inRange(hsv, lower_value_red1, upper_value_red1)
    red_2 = cv2.inRange(hsv, lower_value_red2, upper_value_red2)
    combined = red_1 + red_2

    output = cv2.bitwise_and(frame, frame, mask=combined)

   
    contours, _ = cv2.findContours(combined, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   
    for contour in contours:
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
    cv2.imshow("RED COLOR", frame)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

