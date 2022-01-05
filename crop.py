import os
import cv2
dir = 'images/'
camera = 'left_ori' # or right_ori
os.chdir(dir+camera)
print(os.getcwd())

for i in sorted(os.listdir()):
    img = cv2.resize(cv2.imread(i), (640,480))
    save_path = '../images/' + 'left' + '/' #or right
    cv2.imwrite(save_path+ i, img)