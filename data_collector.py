import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"
labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']
number_of_images = 5

for label_idx, label in enumerate(labels):
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print(f"Error: Unable to access the camera for label '{label}'")
        continue

    print(f"Collecting images for {label}")
    
    # Add extra delay for the first label
    if label_idx == 0:
        print("Extra warm-up time for the first label...")
        time.sleep(5)
    else:
        time.sleep(3)

    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Failed to capture frame for label '{label}'")
            break

        imagename = os.path.join(img_path, f"{label}_{uuid.uuid1()}.jpg")
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()