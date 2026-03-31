from ultralytics import YOLO
import cv2

# load model
model = YOLO("models/yolov8n.pt")

# load image
img = cv2.imread("source_files/construction-safety.jpg")

# prediction
results = model(img)

# show result
for r in results:
    frame = r.plot()

cv2.imshow("PPE Detection", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()