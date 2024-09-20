import cv2
import mediapipe
import pyautogui

capture_hands = mediapipe.solutions.hands.Hands()
drawing_options = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
camera = cv2.VideoCapture(0)
x1 = y1 = x2 = y2 = 0
while True:
  _,image = camera.read()
  image_height , image_width , _ = image.shape
  image = cv2.flip(image,1)
  rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
  output_hands = capture_hands.process(rgb_image)
  all_hands = output_hands.multi_hand_landmarks
  if all_hands:
    for hand in all_hands:
      drawing_options.draw_landmarks(image,hand)
      one_hand_landmark = hand.landmark
      for id , ln in enumerate(one_hand_landmark):
        x =int(ln.x *image_width)
        y = int(ln.y * image_height) 
        if id == 8:
          mouse_x = int(screen_width/ image_width * x)
          mouse_y = int(screen_height/ image_height * y)
          pyautogui.moveTo(mouse_x,mouse_y)
          cv2.circle(image,(x,y),10,(0,255,255))
          x1 = x
          y1 = y
        if id == 4:
          x2 = x
          y2 = y
          cv2.circle(image,(x,y),10,(0,255,255))  
    dist = y2 - y1
    print(dist)  
    if(dist<40):
      pyautogui.click()
      print("Clicked")
  cv2.imshow("Hand Movement video capture",image)
  key = cv2.waitKey(100)
  if key == 27:
    break
camera.release()  
cv2.destroyAllWindows()