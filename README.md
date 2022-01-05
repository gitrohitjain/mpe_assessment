1. Place images captured from left camera in [images/left_ori](https://github.com/gitrohitjain/mpe_assessment/tree/main/images/left_ori) folder and images captured from right camera in [images/right_ori](https://github.com/gitrohitjain/mpe_assessment/tree/main/images/right_ori) folder.
2. Crop images to 640 x 480 to run pretrained model for stereo depth estimation.

python3 crop.py

3. cd stereo_matching
4. Obtain depth map for each frame.

python3 imageDepthEstimation.py
Outputs numpy array of depth map in arrays folder, color disparity image in xrays folder, and  (left,right,color_disparity_img) stacked together in combined folder.

python3 imageDepthEstimation.py

5. 
python3 detect.py --source images/left/ --detection-engine yolov5

