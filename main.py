from ultralytics import YOLO
import cv2, easyocr

# Initialize
model = YOLO("runs/detect/train/weights/best.pt")
reader = easyocr.Reader(["en"], gpu=False)
cap = cv2.VideoCapture("assets/a.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    for box in results[0].boxes.xyxy.cpu().numpy().astype(int):
        x1, y1, x2, y2 = box
        plate = frame[y1:y2, x1:x2]
        ocr = reader.readtext(plate)
        text = " ".join([r[1] for r in ocr])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2
        )
    cv2.imshow("LPR System", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
