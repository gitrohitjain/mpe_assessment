1. Place images captured from left camera in [images/left_ori](https://github.com/gitrohitjain/mpe_assessment/tree/main/images/left_ori) folder and images captured from right camera in [images/right_ori](https://github.com/gitrohitjain/mpe_assessment/tree/main/images/right_ori) folder.

2. Crop images to 640 x 480 to run pretrained model for stereo depth estimation.

3. Obtain depth map for each frame. `python3 stereo_matching/imageDepthEstimation.py` Outputs numpy array of depth map in [images/arrays](https://github.com/gitrohitjain/mpe_assessment/tree/main/images/arrays) folder, color disparity image in [images/xrays](https://github.com/gitrohitjain/mpe_assessment/tree/main/images/xrays) folder, and  (left,right,color_disparity_img) stacked together in [images/combined](https://github.com/gitrohitjain/mpe_assessment/tree/main/images/combined) folder 

![alt text](https://github.com/gitrohitjain/mpe_assessment/blob/main/images/combined/0622.jpg)

4. Here YOLO v5 is used for object detection and I adopt code from Open AI's [CLIP](https://blog.roboflow.com/openai-clip/) to track objects across frames in a video. It uses an object detection model to find items of interest then crops the image and uses CLIP to determine if two detected objects are the same or difference instance of that object across different frames of a video. `python3 detect.py --source images/left/ --detection-engine yolov5`  This outputs [frames](https://github.com/gitrohitjain/mpe_assessment/tree/main/runs/detect) with objects marked with a bounding box with labels of class, tracking id and distance in meter from stereo camera. Here we use depth map array (obtained in step 3) to estimate distance of all detected objects in a frame (after non-max supression.)

<h3>Demo Output</h3>
![alt_text](https://github.com/gitrohitjain/mpe_assessment/blob/main/out_video.gif)

