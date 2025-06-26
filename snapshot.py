import cv2

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()

    if not ret:
        break
    
    cv2.imshow('My Video', frame)
    
    key = cv2.waitKey(1)

    if key == ord('q'):
        break 
    elif key == ord('s'):
        cv2.imwrite('snapshot.png', frame)
        print("Snapshot saved as 'snapshot.png'")

cap.release()
cv2.destroyAllWindows()

