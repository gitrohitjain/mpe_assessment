## Mind Pointeye CV test

### Description:
- We provide a folder "images" containing sequential rectified stereo images with camera information.
- The height of the camera is about 2m. The camera is looking down with a pitch degree of 10 (optional information).
- You need to implement object detection, object tracking, (and maybe stereo matching) on it.
- You are free to use C++, Python, or in a hybrid way.
- You are free to use any off-the-shelf methods (like YOLO, etc).


### Expected outcome
- As shown in the demo video, you are expected to mask a bounding box on each target (pedestrian and vehicle will be enough) and provide the following labels:
   + tracking ID
   + distance (meters) from the bounding box center to the camera optic center

- Due to the time limit, we don't expect the tracking and distance calculation to be very accurate. What we are testing is the overall problem solving capability. 

- Please hand in a video or image sequence folder and your source code so we can have a brief review of your result. Also clarify your environment and library version so that we can re-run it.

- As we don't want to waste your time, you are not required to submit a detailed report, unless you have something to explain.

- If you do not have enough GPU resources, you could use CPU instead and you are not required to run it in real-time.









To run:-
python3 detect.py --source images/left/ --detection-engine yolov5
