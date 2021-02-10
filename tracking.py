import cv2

# Select camera input
cap = cv2.VideoCapture(0)

# Defines track method
tracker = cv2.TrackerCSRT_create()
success, img = cap.read()

# Ask user to select the object in img
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)

# Define draw_box() function to draw a rectangle around the selected object
def draw_box(img, bbox):

    # Set the rectangle coordinates
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3]),
    cv2.rectangle(img,(x,y), ((x+w), (y+h)), (255,0,255), 3, 1)
    cv2.putText(img, "Tracking", (75,75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)


# While True, display img frames as video
while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    success, bbox = tracker.update(img)
    print(bbox)

    # If success, calls draw_box() to draw a rectangle. Else, displays "Lost object."
    if success:
        draw_box(img, bbox)
    else:
        cv2.putText(img, "Lost object", (75,75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    # Calculate and display fps counter
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img, str(int(fps)), (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    # Shows camera image in a 'Tracking' window
    cv2.imshow('Tracking', img)

    # Set 'q' key to close the video
    if cv2.waitKey(1) & 0xff == ord('q'):
        break