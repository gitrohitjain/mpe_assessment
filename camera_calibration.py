import cv2

cam_L_file = cv2.FileStorage("cam_left.yaml", cv2.FILE_STORAGE_READ)
cam_R_file = cv2.FileStorage("cam_right.yaml", cv2.FILE_STORAGE_READ)

camera_matrix_L = cam_L_file.getNode("camera_matrix").mat()
dist_coeff_L = cam_L_file.getNode("distortion_coefficients").mat()
rect_L = cam_L_file.getNode("rectification_matrix").mat()
proj_L = cam_L_file.getNode("projection_matrix").mat()

camera_matrix_R = cam_R_file.getNode("camera_matrix").mat()
dist_coeff_R = cam_R_file.getNode("distortion_coefficients").mat()
rect_R = cam_R_file.getNode("rectification_matrix").mat()
proj_R = cam_R_file.getNode("projection_matrix").mat()


H,W,C = img.shape[0:2]
image_size = (W,H)

# #cam_left.yml
# camera_matrix_L= np.array([[915.583314922979, 0.0, 486.156216093482], [0.0, 913.176127266096, 317.345300339797], [0.0, 0.0, 1.0]])
# dist_coeff_L = np.array([-0.319132360976366, 0.27814804841972, 0.0, 0.0, -0.272034910182435])
# rect_L = np.array([[0.9996897304359291, -0.01599848225199777, -0.01909165856002074], [0.01595237875765353, 0.999869463407055, -0.002564714030888407], [0.01913019793186326, 0.002259360909722831, 0.9998144481929471]])
# proj_L = np.array([[914.754978458673, 0.0, 500.581356048584, 0.0], [0.0, 914.754978458673, 323.8738555908203, 0.0], [0.0, 0.0, 1.0, 0.0]])

# #cam_right.yml
# camera_matrix_R= np.array([[918.360165765321, 0.0, 491.577227643437], [0.0, 916.33382965125, 321.06530759765], [0.0, 0.0, 1.0]])
# dist_coeff_R = np.array([-0.300021351338835, 0.178425245713208, 0.0, 0.0, -0.145246493919359])
# rect_R = np.array([[0.9999619043475868, -0.006242203948765858, 0.006101208356551847], [0.006227026493007892, 0.9999774781767194, 0.002503453691135995], [-0.006116698014731802, -0.002465365934358731, 0.9999782537516534]])
# proj_R = np.array([[914.754978458673, 0.0, 500.581356048584, -457.6941777394], [0.0, 914.754978458673, 323.8738555908203, 0.0], [0.0, 0.0, 1.0, 0.0]])


#METHOD1
###############################

retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F = cv2.stereoCalibrate(obj_points, img_pointsL, img_pointsR, image_size, \
                                                                        camera_matrix_L, dist_coeff_L, camera_matrix_R, dist_coeff_R, flags=cv2.CALIB_FIX_INTRINSIC)


R1, R2, P1, P2, Q, roiL, roiR = cv2.stereoRectify(camera_matrix1=camera_matrix_L , distCoeffs1=dist_coeff_L , camera_matrix2=camera_matrix_R , distCoeffs2=dist_coeff_R ,imageSize=(W,H), R,T, \
                                                                         R1=rect_L, P1=proj_L, R2=rect_R, P2=proj_R, Q=None, alpha=-1, newImageSize=(0,0), R=R, T=T)


# Create undistortion/rectification map for each camera
map1x, map1y = cv2.initUndistortRectifyMap(camera_matrix_L, dist_coeff_L, R1, P1, image_size, cv2.CV_32FC1)
map2x, map2y = cv2.initUndistortRectifyMap(camera_matrix_R, dist_coeff_R, R2, P2, image_size, cv2.CV_32FC1)

img_rect1 = cv2.remap(imgL, mapx1, mapy1, cv2.INTER_LINEAR)
img_rect2 = cv2.remap(imgR.img2, mapx2, mapy2, cv2.INTER_LINEAR)
#################################


# METHOD2
###################
# Refining the camera matrix using parameters obtained by calibration
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix_L, dist_coeff_L, (w,h), 1, (w,h))
corrected_img = cv2.undistort(img.copy(), camera_matrix_L, dist_coeff_L, None, newcameramtx)
