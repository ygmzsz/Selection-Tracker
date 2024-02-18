import cv2

video = cv2.VideoCapture(0)

min_area = 10500

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
_, tresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(tresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_filtred = [c for c in contours if cv2.contourArea(c) > min_area]

fraame = frame.copy()
cv2.drawContours(frame, contours_filtred, -1, (0,255,0),8)

cv2.imshow("counter")

video.release()
cv2.destroyAllWindows