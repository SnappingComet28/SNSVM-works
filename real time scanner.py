import cv2 
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
decoder = cv2.QRCodeDetector()
while True:
    _,frame = cap.read()
    cv2.imshow("QR Scanner",frame)
    if cv2.waitKey(1) & 0xFF == ord('f'):
        break
    output,_,_ = decoder.detectAndDecode(frame)
    if output:
        print(output)
        break
cap.release()
cv2.destroyAllWindows()
