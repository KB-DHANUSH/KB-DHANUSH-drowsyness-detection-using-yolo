from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO('best.pt')

# Open webcamq
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run prediction
    results = model(frame)

    # Render results on frame
    annotated_frame = results[0].plot()

    cv2.imshow('YOLOv8 Webcam Detection', annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
