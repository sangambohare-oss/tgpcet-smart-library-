import cv2
import requests

API_URL = "http://YOUR_SERVER_IP:5000/predict"

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    cv2.imwrite("frame.jpg", frame)

    files = {"image": open("frame.jpg", "rb")}
    res = requests.post(API_URL, files=files)

    print(res.json())

    cv2.imshow("Rover Camera", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()