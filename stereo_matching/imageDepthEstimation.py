import cv2
import os
from hitnet import HitNet, ModelType, draw_disparity, draw_depth, CameraConfig
import numpy as np
from tqdm import tqdm

def main():
	model_type = ModelType.eth3d
	model_path = "models/model_float32.onnx"

	# Initialize model
	hitnet_depth = HitNet(model_path, model_type)

	# Load images
	os.chdir('images/')
	pwd = os.getcwd()
	for f in tqdm(sorted(os.listdir(pwd + '/left'))):
		left_img = cv2.imread(pwd+'/left/'+f)
		right_img = cv2.imread(pwd+'/right/'+f)
		fst = f.split('.')[0]
		# Estimate the depth
		disparity_map = hitnet_depth(left_img, right_img)
		color_disparity = draw_disparity(disparity_map)
		depth_map = hitnet_depth.get_depth()
		np.savetxt(pwd+'/arrays/'+fst, depth_map)
		cv2.imwrite(pwd+'/xrays/'+f, color_disparity)
		combined_image = np.hstack((left_img, right_img, color_disparity))
		cv2.imwrite(pwd+'/combined/'+f, combined_image)
		

if __name__ == '__main__':
	main()
